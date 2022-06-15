from flask import Flask, Blueprint, render_template, redirect, request
from models.manufacturer import Manufacturer
import repositories.manufacturer_repository as manufacturer_repository

manufacturers_blueprint = Blueprint("manufacturers", __name__)

@manufacturers_blueprint.route("/manufacturers", methods = ['GET'])
def show_manufacturers():
    manufacturers = manufacturer_repository.select_all()
    return render_template("manufacturers/index.html", manufacturers = manufacturers)

@manufacturers_blueprint.route("/manufacturers/<id>", methods = ['GET'])
def show_manufacturer(id):
    manufacturer = manufacturer_repository.select(id)
    return render_template("manufacturers/show.html", manufacturer = manufacturer)

@manufacturers_blueprint.route("/manufacturers/new", methods=['GET'])
def new_manufacturer():
    manufacturers = manufacturer_repository.select_all()
    return render_template("manufacturers/new.html", manufacturers = manufacturers)

@manufacturers_blueprint.route("/manufacturers", methods = ["POST"])
def create_manufacturer(): 
    name = request.form['name']
    position = request.form['position']
    country = request.form['country']
    manufacturer = Manufacturer(name, position, country)
    manufacturer_repository.save(manufacturer)
    return redirect('/manufacturers')

@manufacturers_blueprint.route("/manufacturers/<id>/edit", methods=["GET"])
def edit_manufacturer(id):
    manufacturer = manufacturer_repository.select(id)
    manufacturers = manufacturer_repository.select_all()
    return render_template('/manufacturers/edit.html', manufacturer = manufacturer, manufacturers = manufacturers)

@manufacturers_blueprint.route("/manufacturers/<id>", methods = ["POST"])
def update_manufacturer(id): 
    name = request.form['name']
    position = request.form['position']
    quantity = request.form['country']
    manufacturer = Manufacturer(name, position, quantity, id)
    manufacturer_repository.update(manufacturer)
    return redirect('/manufacturers')

@manufacturers_blueprint.route("/manufacturers/<id>/delete", methods = ['POST'])
def delete_manufacturer(id): 
    manufacturer_repository.delete(id)
    return redirect("/manufacturers")

@manufacturers_blueprint.route("/manufacturers/<id>/models", methods=["GET"])
def filter_by(id):
    manufacturer = manufacturer_repository.select(id)
    models = manufacturer_repository.models(manufacturer)
    return render_template("manufacturers/models", manufacturer = manufacturer, models = models)








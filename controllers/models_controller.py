from crypt import methods
from flask import Flask, Blueprint, redirect, render_template, request
from models.manufacturer import Manufacturer 
from models.model import Model
import repositories.model_repository as model_repository
import repositories.manufacturer_repository as manufacturer_repository

models_blueprint = Blueprint("models", __name__)

@models_blueprint.route("/models", methods = ['GET'])
def show_models():
    models = model_repository.select_all()
    return render_template("models/index.html", models = models)

@models_blueprint.route("/models/<id>", methods = ['GET'])
def show_model(id):
    model = model_repository.select(id)
    return render_template("models/show.html", model = model)


@models_blueprint.route("/models/new", methods=['GET'])
def new_model():
    manufacturers = manufacturer_repository.select_all()
    return render_template("models/new.html", manufacturers = manufacturers)

@models_blueprint.route("/models", methods = ["POST"])
def create_model(): 
    name = request.form['name']
    description = request.form['description']
    stock = request.form['stock']
    buy_price = request.form['buy_price']
    sell_price = request.form['sell_price']
    manufacturer_id = request.form['manufacturer_id']
    manufacturer = manufacturer_repository.select(manufacturer_id)
    model = Model(name, description, stock, buy_price, sell_price, manufacturer)
    model_repository.save(model)
    return redirect('/models')

@models_blueprint.route("/models/<id>/edit", methods=["GET"])
def edit_model(id):
    model = model_repository.select(id)
    manufacturers = manufacturer_repository.select_all()
    return render_template('/models/edit.html', model = model, manufacturers = manufacturers)

@models_blueprint.route("/models/<id>", methods = ["POST"])
def update_model(id): 
    name = request.form['name']
    description = request.form['description']
    stock = request.form['stock']
    buy_price = request.form['buy_price']
    sell_price = request.form['sell_price']
    manufacturer_id = request.form['manufacturer_id']
    manufacturer = manufacturer_repository.select(manufacturer_id)
    model = Model(name, description, stock, buy_price, sell_price, manufacturer, id)    
    model_repository.update(model)
    return redirect('/models')

@models_blueprint.route("/models/<id>/delete", methods = ['POST'])
def delete_model(id): 
    model_repository.delete(id)
    return redirect("/models")

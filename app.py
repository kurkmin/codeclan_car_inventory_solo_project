from flask import Flask, render_template
import repositories.manufacturer_repository as manufacturer_repository
import repositories.model_repository as model_repository

from controllers.manufacturers_controller import manufacturers_blueprint
from controllers.models_controller import models_blueprint
app = Flask(__name__)

app.register_blueprint(manufacturers_blueprint)
app.register_blueprint(models_blueprint)

@app.route("/")
def main():
    return render_template("index.html")

if __name__ == "__main__":
    app.run()
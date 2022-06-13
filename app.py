from flask import Flask, render_template

from controllers.manufacturers_controller import manufacturers_blueprint
from controllers.models_controller import models_blueprint
app = Flask(__name__)

app.register_blueprint(manufacturers_blueprint)
app.register_blueprint(models_blueprint)

@app.route("/")
def main():
    return render_template("index.html", title = "home") 

if __name__ == "__main__":
    app.run()
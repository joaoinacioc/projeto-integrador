from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from routes.blueprint import blueprint
from models.cliente import db

'''app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://'


@app.route("/")
def home():
    return render_template("home.html")


@app.route("/cliente/<nome_cliente>")
def client(nome_cliente):
   return render_template("cliente.html", nome_cliente=nome_cliente)


if __name__ == "__main__":
    app.run(debug=True)'''

def create_app():
   app = Flask(__name__)  # flask app object
   app.config.from_object('config')  # Configuring from Python Files

   db.init_app(app)  # Initializing the database
   return app


app = create_app()  # Creating the app
 #Registering the blueprint
app.register_blueprint(blueprint, url_prefix='/')
migrate = Migrate(app, db)  # Initializing the migration


if __name__ == '__main__':  # Running the app
    app.run(host='127.0.0.1', port=5000, debug=True)
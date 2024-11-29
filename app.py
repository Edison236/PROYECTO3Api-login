from flask import Flask, render_template
from dotenv import load_dotenv
from databases.db import db,init_db
from controllers.controller_product import product_bp
from controllers.controller_ingredient import ingredient_bp
from flask_login import LoginManager
import os 
import secrets

load_dotenv()
login_manager = LoginManager()
app = Flask(__name__, template_folder="views")

SECRET_KEY = secrets.token_urlsafe(32)
app.config["SQLALCHEMY_DATABASE_URI"] = f"mysql+pymysql://{os.getenv('DB_USERNAME')}:{os.getenv('DB_PASSWORD')}@{os.getenv('DB_HOST')}:{os.getenv('DB_PORT')}/{os.getenv('DB_NAME')}"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db.init_app(app)
init_db(app)
login_manager.init_app(app)

# Blueprint
app.register_blueprint(product_bp)
app.register_blueprint(ingredient_bp)

@app.route("/")
def index():
    return render_template("index.html")

if __name__ == '__main__':    
    app.run(debug=True)
    
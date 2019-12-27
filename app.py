from flask import Flask
from flask_cors import CORS
from extensions import db
from environment import DB_USERNAME, DB_PASSWORD, DB_NAME
from controllers.authentication import authentication


app = Flask(__name__)
cors = CORS(app)

app.config["DEBUG"] = True
app.config[
    "SQLALCHEMY_DATABASE_URI"
] = f"mysql+pymysql://{DB_USERNAME}:{DB_PASSWORD}@localhost:3306/{DB_NAME}"
app.config["SQLALCHEMY_ECHO"] = True
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

app.register_blueprint(authentication)

db.init_app(app)

if __name__ == "__main__":
    app.run()


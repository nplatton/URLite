from flask import Flask
from flask_cors import CORS

# from db_config import Config

app = Flask(__name__)
CORS(app)
# app.config.from_object(Config)

from app import routes
from app import errors

if __name__ == "__main__":
    app.run(debug = True)

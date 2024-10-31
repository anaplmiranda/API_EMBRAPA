from flask import Flask, request, jsonify
from flasgger import Swagger
from flask_httpauth import HTTPBasicAuth


auth = HTTPBasicAuth()

app = Flask(__name__)
swagger = Swagger(app)

from app.utils import auth as auth_utils
from app.routes import auth_routes, scrape_routes

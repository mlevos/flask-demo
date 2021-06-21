#!/usr/bin/env python

# NOTE: Run with PYTHONPATH=. python example/app.py

from flask import Flask
from flask_cors import CORS

from flask_restful_swagger_3 import Api, swagger, get_swagger_blueprint

from .views import BooksResouce
from .conf import *


app = Flask(__name__)
CORS(app)


servers = [{"url": f'{PROTOCOL}://{HOST}:{PORT}'}]
api = Api(app, version='5', servers=servers, title=f"{APP_NAME}")




swagger_blueprint = get_swagger_blueprint(
    api.open_api_object,
    swagger_prefix_url=SWAGGER_URL,
    swagger_url=API_URL)


api.add_resource(BooksResouce, '/books')

app.register_blueprint(swagger_blueprint)

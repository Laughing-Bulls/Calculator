"""A simple flask web app"""
from flask import Flask
from werkzeug.debug import DebuggedApplication
from app.controllers.index_controller import IndexController
from app.controllers.calculator_controller import CalculatorController
from app.controllers.oop_controller import OopController
from app.controllers.four_controller import FourController
from app.controllers.table_controller import TableController


app = Flask(__name__)
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'
app.wsgi_app = DebuggedApplication(app.wsgi_app, True)


@app.route("/", methods=['GET'])
def index_get():
    return IndexController.get()

@app.route("/calculator", methods=['GET'])
def calculator_get():
    return CalculatorController.get()

@app.route("/calculator", methods=['POST'])
def calculator_post():
    return CalculatorController.post()

@app.route("/oop", methods=['GET'])
def oop_get():
    return OopController.get()

@app.route("/table", methods=['GET'])
def table_get():
    return TableController.get()

@app.errorhandler(404)
def page_not_found(e):
    return FourController.get()
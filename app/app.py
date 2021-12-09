"""A simple flask web app"""
from flask import Flask
from werkzeug.debug import DebuggedApplication
from app.controllers.index_controller import IndexController
from app.controllers.calculator_controller import CalculatorController
from app.controllers.oop_controller import OopController
from app.controllers.four_controller import FourController
from app.controllers.numtable_controller import NumTableController
from app.controllers.browser_controller import BrowserController
from app.controllers.isp_controller import ISPController
from app.controllers.salesmen_controller import SalesmenController
from app.controllers.builders_controller import BuildersController

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

@app.route("/numtable", methods=['GET'])
def numtable_get():
    return NumTableController.get()

@app.errorhandler(404)
def page_not_found(e):
    return FourController.get()

@app.route("/browsers", methods=['GET'])
def browsers_get():
    return BrowserController.get()

@app.route("/isp", methods=['GET'])
def isp_get():
    return ISPController.get()

@app.route("/salesmen", methods=['GET'])
def salesmen_get():
    return SalesmenController.get()

@app.route("/builders", methods=['GET'])
def builders_get():
    return BuildersController.get()

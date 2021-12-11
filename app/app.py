"""A simple flask web app"""
# pylint: disable=import-error,no-name-in-module
from flask import Flask
from werkzeug.debug import DebuggedApplication
from app.controllers.index_controller import IndexController
from app.controllers.calculator_controller import CalculatorController
from app.controllers.oop_controller import OopController
from app.controllers.four_controller import FourController
from app.controllers.numtable_controller import NumTableController
from app.controllers.battle_controller import BattleController
from app.controllers.people_controller import PeopleController
from app.controllers.browser_controller import BrowserController
from app.controllers.isp_controller import ISPController
from app.controllers.search_controller import SearchController
from app.controllers.salesmen_controller import SalesmenController
from app.controllers.builders_controller import BuildersController
from app.controllers.enablers_controller import EnablersController


app = Flask(__name__)
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'
app.wsgi_app = DebuggedApplication(app.wsgi_app, True)


@app.route("/", methods=['GET'])
def index_get():
    """ For index.html (home page)"""
    return IndexController.get()


@app.route("/calculator", methods=['GET'])
def calculator_get():
    """ For calculator.html (calculator input page)"""
    return CalculatorController.get()


@app.route("/calculator", methods=['POST'])
def calculator_post():
    """ For calculator.html (post to calculator input page)"""
    return CalculatorController.post()


@app.route("/numtable", methods=['GET'])
def numtable_get():
    """ For numtable.html (calculator history table output page)"""
    return NumTableController.get()


@app.route("/battle", methods=['GET'])
def battle_get():
    """ For battle.html (battles of the Internet z-page)"""
    return BattleController.get()


@app.route("/browsers", methods=['GET'])
def browsers_get():
    """ For browsers.html (battle of the browsers page)"""
    return BrowserController.get()


@app.route("/isp", methods=['GET'])
def isp_get():
    """ For isp.html (battle of the ISPs page)"""
    return ISPController.get()


@app.route("/search", methods=['GET'])
def search_get():
    """ For search.html (battle of the search engines page)"""
    return SearchController.get()


@app.route("/people", methods=['GET'])
def people_get():
    """ For people.html (people of the Internet z-page)"""
    return PeopleController.get()


@app.route("/salesmen", methods=['GET'])
def salesmen_get():
    """ For salesmen.html (people behind the early Internet - salesmen page)"""
    return SalesmenController.get()


@app.route("/builders", methods=['GET'])
def builders_get():
    """ For builders.html (people behind the early Internet - builders page)"""
    return BuildersController.get()


@app.route("/enablers", methods=['GET'])
def enablers_get():
    """ For enablers.html (people behind the early Internet - enablers page)"""
    return EnablersController.get()


@app.route("/oop", methods=['GET'])
def oop_get():
    """ For oop.html (object oriented programming principles page)"""
    return OopController.get()


@app.errorhandler(404)
def page_not_found():
    """ For 404.html (page not found page)"""
    return FourController.get()

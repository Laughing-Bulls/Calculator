"""Flask web controller for People of the Internet z-page"""
# pylint: disable=import-error,no-name-in-module,too-few-public-methods
from flask import render_template
from app.controllers.controller import ControllerBase


class PeopleController(ControllerBase):
    """Page controller"""
    @staticmethod
    def get():
        """ This method will render the People z-page"""
        return render_template('people.html')

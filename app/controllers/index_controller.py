"""Flask web controller for index (home) page"""
# pylint: disable=import-error,no-name-in-module,too-few-public-methods
from flask import render_template
from app.controllers.controller import ControllerBase


class IndexController(ControllerBase):
    """Page controller"""
    @staticmethod
    def get():
        """ This method will render the index page (home page)"""
        return render_template('index.html')

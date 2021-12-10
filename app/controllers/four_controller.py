"""Flask web controller for 404 error page"""
# pylint: disable=import-error,no-name-in-module,too-few-public-methods
from flask import render_template
from app.controllers.controller import ControllerBase


class FourController(ControllerBase):
    """Page controller"""
    @staticmethod
    def get():
        """ This method will render a 404 error page (page not found)"""
        return render_template('404.html')

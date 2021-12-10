"""Flask web controller for object oriented programming principles page"""
# pylint: disable=import-error,no-name-in-module,too-few-public-methods
from flask import render_template
from app.controllers.controller import ControllerBase


class SalesmenController(ControllerBase):
    """Page controller"""
    @staticmethod
    def get():
        """ This method will render the Salesmen page"""
        return render_template('salesmen.html')

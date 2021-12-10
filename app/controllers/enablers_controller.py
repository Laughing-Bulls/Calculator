"""Flask web controller for enablers of the Internet page"""
# pylint: disable=import-error,no-name-in-module,too-few-public-methods
from flask import render_template
from app.controllers.controller import ControllerBase


class EnablersController(ControllerBase):
    """Page controller"""
    @staticmethod
    def get():
        """ This method will render the Enablers page"""
        return render_template('enablers.html')

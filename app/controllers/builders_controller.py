"""Flask web controller for builders of the Internet page"""
# pylint: disable=import-error,no-name-in-module,too-few-public-methods
from flask import render_template
from app.controllers.controller import ControllerBase


class BuildersController(ControllerBase):
    """Page controller"""
    @staticmethod
    def get():
        """ This method will render the Builders page"""
        return render_template('builders.html')

"""Flask web controller for battle of the browsers page"""
# pylint: disable=import-error,no-name-in-module,too-few-public-methods
from flask import render_template
from app.controllers.controller import ControllerBase


class BrowserController(ControllerBase):
    @staticmethod
    def get():
        """ This method will render the Browser page"""
        return render_template('browsers.html')

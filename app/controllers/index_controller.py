"""Flask web controller for index (home) page"""
# pylint: disable=import-error,no-name-in-module,too-few-public-methods
from flask import render_template, flash
from app.controllers.controller import ControllerBase


class IndexController(ControllerBase):
    @staticmethod
    def get():
        """ This method will render the index page (home page)"""
        return render_template('index.html')

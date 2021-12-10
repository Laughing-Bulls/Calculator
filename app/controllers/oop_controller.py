"""Flask web controller for object oriented programming principles page"""
# pylint: disable=import-error,no-name-in-module,too-few-public-methods
from flask import render_template
from app.controllers.controller import ControllerBase


class OopController(ControllerBase):
    @staticmethod
    def get():
        """ This method will render the Object Oriented Programming page"""
        return render_template('oop.html')

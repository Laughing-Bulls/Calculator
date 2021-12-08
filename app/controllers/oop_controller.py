from app.controllers.controller import ControllerBase
from flask import render_template


class OopController(ControllerBase):
    @staticmethod
    def get():
        """ This method will render the Object Oriented Programming page"""
        return render_template('oop.html')

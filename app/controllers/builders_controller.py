from app.controllers.controller import ControllerBase
from flask import render_template


class BuildersController(ControllerBase):
    @staticmethod
    def get():
        """ This method will render the Builders page"""
        return render_template('builders.html')

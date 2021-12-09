from app.controllers.controller import ControllerBase
from flask import render_template, flash


class IndexController(ControllerBase):
    @staticmethod
    def get():
        """ This method will render the index page (home page)"""
        return render_template('index.html')

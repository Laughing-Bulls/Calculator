from app.controllers.controller import ControllerBase
from flask import render_template


class FourController(ControllerBase):
    @staticmethod
    def get():
        """ This method will render a 404 error page (page not found)"""
        return render_template('404.html')

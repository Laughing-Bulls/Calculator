from app.controllers.controller import ControllerBase
from flask import render_template


class BrowserController(ControllerBase):
    @staticmethod
    def get():
        """ This method will render the Browser page"""
        return render_template('browsers.html')

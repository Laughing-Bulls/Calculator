from app.controllers.controller import ControllerBase
from flask import render_template


class SalesmenController(ControllerBase):

    @staticmethod
    def get():
        """ This method will render the Salesmen page"""
        return render_template('salesmen.html')

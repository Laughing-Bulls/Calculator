from app.controllers.controller import ControllerBase
from flask import render_template


class TableController(ControllerBase):
    @staticmethod
    def get():
        """ This method will render the Table Output page"""
        return render_template('table.html')

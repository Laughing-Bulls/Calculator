from app.controllers.controller import ControllerBase
from flask import render_template


class FourController(ControllerBase):
    @staticmethod
    def get():
        return render_template('404.html')

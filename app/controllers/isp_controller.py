from app.controllers.controller import ControllerBase
from flask import render_template


class ISPController(ControllerBase):
    @staticmethod
    def get():
        """ This method will render the ISP page"""
        return render_template('isp.html')

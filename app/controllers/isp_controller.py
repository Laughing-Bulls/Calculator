"""Flask web controller for Battle of the ISPs page"""
# pylint: disable=import-error,no-name-in-module,too-few-public-methods
from flask import render_template
from app.controllers.controller import ControllerBase


class ISPController(ControllerBase):
    """Page controller"""
    @staticmethod
    def get():
        """ This method will render the ISP page"""
        return render_template('isp.html')

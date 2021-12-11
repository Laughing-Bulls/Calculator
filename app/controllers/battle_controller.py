"""Flask web controller for Battles of the Internet z-page"""
# pylint: disable=import-error,no-name-in-module,too-few-public-methods
from flask import render_template
from app.controllers.controller import ControllerBase


class BattleController(ControllerBase):
    """Page controller"""
    @staticmethod
    def get():
        """ This method will render the Battles z-page"""
        return render_template('battle.html')

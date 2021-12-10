"""Flask web controller for battle of the search engines page"""
# pylint: disable=import-error,no-name-in-module,too-few-public-methods
from flask import render_template
from app.controllers.controller import ControllerBase


class SearchController(ControllerBase):
    """Page controller"""
    @staticmethod
    def get():
        """ This method will render the Search Battles page"""
        return render_template('search.html')

"""Flask web controller for calculator history table display page"""
# pylint: disable=import-error,no-name-in-module,too-few-public-methods
from flask import render_template
from filehandling.fileops import Fileops
from app.controllers.controller import ControllerBase


class NumTableController(ControllerBase):
    """Page controller"""

    @staticmethod
    def get():
        """ This method will render the Table Output page"""
        answer_df = Fileops.calculate_history_file("calculation-history.csv")
        return render_template('numtable.html', cols=answer_df.columns.values,
                               row_data=list(answer_df.values.tolist()), zip=zip)

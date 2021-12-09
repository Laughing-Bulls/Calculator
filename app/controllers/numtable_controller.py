from app.controllers.controller import ControllerBase
from flask import render_template, flash
from filehandling.filehandling import Filehandling


class NumTableController(ControllerBase):
    @staticmethod
    def get():
        """ This method will render the Table Output page"""
        answer_df = Filehandling.retrieve_df_from_file("calculation-output.csv")
        return render_template('numtable.html', cols=answer_df.columns.values,
                               row_data=list(answer_df.values.tolist()), zip=zip)

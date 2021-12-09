from app.controllers.controller import ControllerBase
from flask import Flask, render_template
import pandas as pd
from filehandling.filehandling import Filehandling
# from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:/home/myuser/data/db.sqlite'
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///home/myuser/data/db.sqlite'
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


# answer_df = Filehandling.retrieve_df_from_file("1-addition-ex-large.csv")
# answer_df.to_html(header="true", table_id="table")

"""
class Calculation(answer_df):
    # This class handles database operations
    value1 = answer_df.Column(db.Integer, primary_key=True)
    value2 = answer_df.Column(db.String(64), index=True)
    value3 = answer_df.Column(db.Integer, index=True)
    operator = answer_df.Column(db.String(256), index=True)
    answer = answer_df.Column(db.String(120), index=True)
"""

class NumTableController(ControllerBase):
    @staticmethod
    def get():
        """ This method will render the Table Output page"""
        # calculations = Calculation.query
        answer_df = Filehandling.retrieve_df_from_file("calculation-output.csv")
        return render_template('numtable.html', title='Answers in a Bootstrap Table',
                                cols=answer_df.columns.values, row_data=list(answer_df.values.tolist()), zip=zip)
                                # tables=[answer_df.to_html(classes="data")], header="false", index="false")
                                # tables=[answer_df.to_html(classes="data")], titles=answer_df.columns.values)


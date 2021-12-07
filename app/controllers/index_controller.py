from app.controllers.controller import ControllerBase
from flask import render_template, flash


class IndexController(ControllerBase):
    @staticmethod
    def get():
        flash("ALERT: FLASH TEST")
        return render_template('index.html')

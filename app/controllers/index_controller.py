from app.controllers.controller import ControllerBase
from flask import render_template


class IndexController(ControllerBase):
    @staticmethod
    def get():
        return render_template('index.html')

class DummyClass(ControllerBase):
    @staticmethod
    def just_testing_this():
        return render_template('oop.html')

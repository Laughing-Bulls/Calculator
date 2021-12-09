from app.controllers.controller import ControllerBase
from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:/home/myuser/data/db.sqlite'
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///home/myuser/data/db.sqlite'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class User(db.Model):
    """ This class handles database operations"""
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), index=True)
    age = db.Column(db.Integer, index=True)
    address = db.Column(db.String(256))
    phone = db.Column(db.String(20))
    email = db.Column(db.String(120), index=True)


db.create_all()


class TableController(ControllerBase):
    @staticmethod
    def get():
        """ This method will render the Table Output page"""
        users = User.query
        return render_template('table.html', title='Bootstrap Table',
                               users=users)

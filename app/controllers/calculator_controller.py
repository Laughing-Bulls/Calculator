from app.controllers.controller import ControllerBase
from filehandling.fileops import Fileops
# from calc.calculator import Calculator

from flask import Flask, render_template, request, flash, redirect, url_for


class CalculatorController(ControllerBase):
    @staticmethod
    def post():
        """ This method will render the calculator page following a post command - data inputted"""
        # get the values out of the form
        value1 = request.form['value1']
        value2 = request.form['value2']
        value3 = request.form['value3']
        operation = request.form['operation']
        is_no_error = True
        error = ""

        # make sure first two input values contain numbers or return error and reload page
        try:
            value1 = float(value1)
            value2 = float(value2)
        except ValueError:
            is_no_error = False
            error = 'ERROR: You must enter a numerical value for value 1 and value 2'

        if is_no_error:
            # make the tuple
            try:
                value3 = float(value3)
                input_tuple = (value1, value2, value3)
            except ValueError:
                value3 = ""
                input_tuple = (value1, value2)

            # calculate result and add to history file
            result = str(Fileops.add_calculation_to_history_file(input_tuple, operation))

            # note any computation errors with flash messages
            if operation == "division" and result == "None":
                is_no_error = False
                error = 'ERROR: Division by zero is not allowed'
            if operation == "exponent" and result == "None":
                is_no_error = False
                error = 'ERROR: Inputs are too large for exponent calculation'
            if is_no_error:
                flash("Calculation Successful!")

            return render_template('result.html', value1=value1, value2=value2, value3=value3, operation=operation,
                                   result=result, error=error)
        else:
            return render_template('calculator.html', error=error)

    @staticmethod
    def get():
        """ This method will render the calculator page, which asks user for inputs"""
        return render_template('calculator.html')

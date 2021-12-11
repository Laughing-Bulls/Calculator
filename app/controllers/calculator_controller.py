"""Flask web controller for the Web Calculator page"""
# pylint: disable=import-error,no-name-in-module
from flask import render_template, request, flash
from app.controllers.controller import ControllerBase
from filehandling.filehandling import Filehandling
from filehandling.fileops import Fileops


class CalculatorController(ControllerBase):
    """Page controller"""

    @staticmethod
    def post():
        """ This method renders the calculator page following a post command - data inputted"""
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
            # make the tuple and add to history file
            try:
                value3 = float(value3)
                input_tuple = (value1, value2, value3)
            except ValueError:
                value3 = ""
                input_tuple = (value1, value2)

            # add inputs to history file
            Filehandling.make_history_log_entry(input_tuple, operation)
            # calculate result
            result = Fileops.get_calculation_result(input_tuple, operation)
            # note any computation errors with flash messages
            if operation == "division" and result == "Error":
                is_no_error = False
                error = 'ERROR: Division by zero is not allowed'
            if operation == "exponent" and result == "Error":
                is_no_error = False
                error = 'ERROR: Inputs are too large for exponent calculation'
            if is_no_error:
                flash("Calculation Successful!")

            return render_template('result.html', value1=value1, value2=value2, value3=value3,
                                   operation=operation, result=result, error=error)

        return render_template('calculator.html', error=error)

    @staticmethod
    def get():
        """ This method will render the calculator page, which asks user for inputs"""
        return render_template('calculator.html')

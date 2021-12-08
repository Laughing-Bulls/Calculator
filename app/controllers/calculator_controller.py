from app.controllers.controller import ControllerBase
from calc.calculator import Calculator
from flask import Flask, render_template, request, flash, redirect, url_for


class CalculatorController(ControllerBase):
    @staticmethod
    def post():
        """ This method will render the calculator page following a post command - data inputted"""
        # get the values out of the form
        value1 = request.form['value1']
        value2 = request.form['value2']
        operation = request.form['operation']
        is_error = False
        message = 'Calculation successful. This calculator is awesome!'
        try:
            value1 = float(value1)
            value2 = float(value2)
        except ValueError:
            is_error = True
            message = 'ERROR: You must enter a numerical value for value 1 and value 2'
        if operation == "division" and value2 == 0.0:
            is_error = True
            message = 'ERROR: Division by zero is not allowed'
        if is_error == False:
            flash(message)
            # make the tuple
            my_tuple = (value1, value2)
            # call the correct operation
            getattr(Calculator, operation)(my_tuple)
            # get calculation result from History
            result = str(Calculator.get_last_result_value())
            return render_template('result.html', value1=value1, value2=value2, operation=operation, result=result)
        else:
            return render_template('calculator.html', error=message)

    @staticmethod
    def get():
        """ This method will render the calculator page, which asks user for inputs"""
        return render_template('calculator.html')

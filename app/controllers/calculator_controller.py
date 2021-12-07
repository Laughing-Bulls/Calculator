from app.controllers.controller import ControllerBase
from calc.calculator import Calculator
from flask import Flask, render_template, request, flash, redirect, url_for


class CalculatorController(ControllerBase):
    @staticmethod
    def post():
        if request.form['value1'] != "" and request.form['value2'] != "":
            flash('Calculation successful. This calculator is awesome!')
            # get the values out of the form
            value1 = request.form['value1']
            value2 = request.form['value2']
            operation = request.form['operation']
            if operation == "division" and value2 == 0:
                result = "Division by zero is not allowed"
            else:
                # make the tuple
                my_tuple = (value1, value2)
                # this will call the correct operation
                getattr(Calculator, operation)(my_tuple)
                result = str(Calculator.get_last_result_value())
            return render_template('result.html', value1=value1, value2=value2, operation=operation, result=result)
        else:
            error = 'ERROR: You must enter a numerical value for value 1 and value 2'
            return render_template('calculator.html', error=error)

    @staticmethod
    def get():
        return render_template('calculator.html')

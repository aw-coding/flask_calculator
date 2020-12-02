from app import app

from modules.calculator import *


@app.route("/")
def print_a_message():
    return "hello"

@app.route("/add/<num1>/<num2>")
def add_in_browser(num1, num2):
    return f"this equals {add(num1, num2)}"

@app.route("/subtract/<num1>/<num2>")
def subtract_in_browser(num1, num2):
    return f"this equals {subtract(num1, num2)}"

@app.route("/multiply/<num1>/<num2>")
def multiply_in_browser(num1, num2):
    return f"this equals {multiply(num1, num2)}"

@app.route("/divide/<num1>/<num2>")
def divide_in_browser(num1, num2):
    return f"this equals {divide(num1, num2)}"        



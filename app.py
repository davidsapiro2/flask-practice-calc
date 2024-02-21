from flask import Flask, request

app = Flask(__name__)

from operations import add, sub, mult, div

# Expect localhost:5000/add?a=[num]&b=[num]
@app.get("/add")
def add_route():
    num1 = int(request.args["a"])
    num2 = int(request.args["b"])
    return f"{add(num1, num2)}"

# Expect localhost:5000/sub?a=[num]&b=[num]
@app.get("/sub")
def sub_route():
    num1 = int(request.args["a"])
    num2 = int(request.args["b"])
    return f"{sub(num1, num2)}"

# Expect localhost:5000/mult?a=[num]&b=[num]
@app.get("/mult")
def mult_route():
    num1 = int(request.args["a"])
    num2 = int(request.args["b"])
    return f"{mult(num1, num2)}"

# Expect localhost:5000/div?a=[num]&b=[num]
@app.get("/div")
def div_route():
    num1 = int(request.args["a"])
    num2 = int(request.args["b"])
    return f"{div(num1, num2)}"

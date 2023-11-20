from flask import Flask
import math

app = Flask(__name__)

def calculate_factorial(number):
    result = 1
    for i in range(1, number + 1):
        result *= i
    return result

@app.route('/')
def hello():
    return 'Hello, this is a Flask app!'

@app.route('/stress')
def stress():
    # Generate high CPU load by calculating the factorial of a large number
    result = calculate_factorial(10000)
    return f'Stress test complete! Result: {result}'
from flask import Flask, render_template, request
import math

app = Flask(__name__)

def calculate(op, x, y=None):
    try:
        x = float(x)
        y = float(y) if y else None
        if op == 'add':
            return x + y
        elif op == 'subtract':
            return x - y
        elif op == 'multiply':
            return x * y
        elif op == 'divide':
            return x / y if y != 0 else "Error"
        elif op == 'power':
            return math.pow(x, y)
        elif op == 'sqrt':
            return math.sqrt(x)
        elif op == 'sin':
            return math.sin(math.radians(x))
        elif op == 'cos':
            return math.cos(math.radians(x))
        elif op == 'tan':
            return math.tan(math.radians(x))
        elif op == 'log':
            return math.log(x, y if y else 10)
        elif op == 'exp':
            return math.exp(x)
        else:
            return "Invalid operation"
    except Exception:
        return "Error"

@app.route("/", methods=["GET", "POST"])
def index():
    result = None
    if request.method == "POST":
        op = request.form["operation"]
        x = request.form["x"]
        y = request.form.get("y")
        result = calculate(op, x, y)
    return render_template("index.html", result=result)

if __name__ == "__main__":
    app.run(debug=True)
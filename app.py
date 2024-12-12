from flask import Flask, render_template, request, redirect, url_for, jsonify

app = Flask(__name__)


def add_numbers(a, b):
    """Adds two numbers and returns the result."""
    if isinstance(a, bool) or isinstance(b, bool):
        raise TypeError("Boolean values are not allowed")
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError("Both inputs must be int or float")
    return a + b

def multiply_numbers(a, b):
    """Multiplies two numbers and returns the result."""
    if isinstance(a, bool) or isinstance(b, bool):
        raise TypeError("Boolean values are not allowed")
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError("Both inputs must be int or float")
    return a * b


@app.route('/')
def index():
    """Render the main page with forms."""
    return render_template('index.html')

@app.route('/calculate', methods=['POST'])
def calculate():
    """Handle form submission and display the result."""
    operation = request.form.get('operation')
    a = request.form.get('a')
    b = request.form.get('b')
    c = request.form.get('c')

    try:
        a = float(a)
        b = float(b)
        # Perform the selected operation
        if operation == 'add':
            result = add_numbers(a, b)
            return render_template('result.html', result=result)
        elif operation == 'multiply':
            result = multiply_numbers(a, b)
            return render_template('result.html', result=result)
        elif operation == 'add_multiply':
            c = float(c)
            sum_result = add_numbers(a, b)
            result = multiply_numbers(sum_result, c)
            return render_template('result.html', result=result)
        else:
            return render_template('result.html', error="Invalid operation selected.")
    except (TypeError, ValueError):
        return render_template('result.html', error="Invalid input provided.")

@app.route('/add', methods=['GET'])
def add():
    """API endpoint to add two numbers."""
    try:
        a = float(request.args.get('a'))
        b = float(request.args.get('b'))
        result = add_numbers(a, b)
        return jsonify({'result': result})
    except (TypeError, ValueError):
        return jsonify({'error': 'Invalid input'}), 400

@app.route('/multiply', methods=['GET'])
def multiply():
    """API endpoint to multiply two numbers."""
    try:
        a = float(request.args.get('a'))
        b = float(request.args.get('b'))
        result = multiply_numbers(a, b)
        return jsonify({'result': result})
    except (TypeError, ValueError):
        return jsonify({'error': 'Invalid input'}), 400

@app.route('/add_multiply', methods=['GET'])
def add_and_multiply():
    """API endpoint to add two numbers and then multiply the result by a third number."""
    try:
        a = float(request.args.get('a'))
        b = float(request.args.get('b'))
        c = float(request.args.get('c'))
        sum_result = add_numbers(a, b)
        final_result = multiply_numbers(sum_result, c)
        return jsonify({'result': final_result})
    except (TypeError, ValueError):
        return jsonify({'error': 'Invalid input'}), 400

if __name__ == '__main__':
    app.run(debug=True)
from flask import Flask, render_template, request, url_for
from werkzeug.utils import redirect

# Prediction module
from flask_wrapper.predict import *

# Flask instance
app = Flask(__name__)

# Home page, index.html
@app.route('/')
def home():
    return render_template('index.html')

# Show the result
@app.route('/output', methods = ['POST', 'GET'])
def output():
    if request.method == 'POST':
        x = None
        try:
            float(request.form['x'])
        except ValueError:
            return render_template('error.html')
        else:
            x = float(request.form['x'])

            output = predict(x)
            output = round(output[0], 2)

    return render_template('output.html', input = str(x), output = str(output))
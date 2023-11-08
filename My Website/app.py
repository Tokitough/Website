from flask import Flask, render_template, request
import math

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/profile')
def profile():
    return render_template('profile.html')

@app.route('/toUpperCase', methods=['GET', 'POST'])
def toUpperCase():
    result = None
    if request.method == 'POST':
        input_string = request.form.get('inputString', '')
        result = input_string.upper()
    return render_template('touppercase.html', result=result)

@app.route('/works')
def works():
    return render_template('works.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/areaOfcircle', methods=['GET', 'POST'])
def areaOfCircle():
    areaOfCircle = None
    if request.method == 'POST':
        radius = request.form.get('inputRadius', '')
        areaOfCircle = math.pi * (int(radius) * int(radius))
        areaOfCircle = "%.2f" % areaOfCircle
    return render_template('areaOfcircle.html', areaOfCircle=areaOfCircle)

@app.route('/areaOfTriangle', methods=['GET', 'POST'])
def areaOfTriagle():
    areaOfTriangle = None
    if request.method == 'POST':
        base = request.form.get('inputBase', '')
        height = request.form.get('inputHeight', '')
        areaOfTriangle = 0.5 * (int(base) * int(height))
        areaOfTriangle = "%.2f" % areaOfTriangle
    return render_template('areaOfTriangle.html', areaOfTriangle=areaOfTriangle)

if __name__ == "__main__":
    app.run(debug=True)

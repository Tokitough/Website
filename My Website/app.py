from flask import Flask, render_template, request, jsonify
from merge_linked_lists import merge_sorted_lists, print_linked_list, create_linked_list
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

@app.route('/mergeLinkedLists', methods=['GET', 'POST'])
def merge():
    result_values = None
    error = None
    list1 = None
    list2 = None

    if request.method == 'POST':
        try:
            size1 = int(request.form.get('size1', 0))
            values1 = [val.strip() for val in request.form.get('values1', '').split(',')]
            if size1 != len(values1):
                raise ValueError("Size should be equal to the number of values for Linked List 1.")
            list1 = create_linked_list(size1, values1)

            size2 = int(request.form.get('size2', 0))
            values2 = [val.strip() for val in request.form.get('values2', '').split(',')]
            if size2 != len(values2):
                raise ValueError("Size should be equal to the number of values for Linked List 2.")
            list2 = create_linked_list(size2, values2)

            result_values = merge_sorted_lists(list1, list2)

        except ValueError as e:
            error = str(e)

    return render_template('mergelinkedlists.html', result_values=result_values, error=error, print_linked_list=print_linked_list, list1=list1, list2=list2)

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

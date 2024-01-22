from flask import Flask, render_template, request, jsonify
import math

app = Flask(__name__)

class ListNode:
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next

def merge_sorted_lists(list1, list2):
    # dummy node to serve as head of merge list
    dummy = ListNode()
    current = dummy
	
	# Check both lists and compare the values
    while list1 is not None and list2 is not None:
        if list1.value <= list2.value:
            current.next = list1
            list1 = list1.next
        else:
            current.next = list2
            list2 = list2.next

  		# move to the current node
        current = current.next

	# If any of the list gets completely empty
    # directly join all the elements of the other list
    if list1 is None:
        current.next = list2
    elif list2 is None:
        current.next = list1

    return dummy.next

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

@app.route('/mergeLinkedLists')
def merge_lists_endpoint():
    data = request.get_json(force=True)
    print(data)

    # Assuming data contains two lists in the format {'list1': [1, 3, 5], 'list2': [2, 4, 6]}
    list1_values = data.get('list1', [])
    list2_values = data.get('list2', [])

    # Convert input lists to linked lists
    list1 = ListNode()
    current1 = list1
    for value in list1_values:
        current1.next = ListNode(value)
        current1 = current1.next

    list2 = ListNode()
    current2 = list2
    for value in list2_values:
        current2.next = ListNode(value)
        current2 = current2.next

    # Merge the linked lists
    merged_list = merge_sorted_lists(list1.next, list2.next)

    # Convert the merged list back to a Python list
    result = []
    current = merged_list
    while current:
        result.append(current.value)
        current = current.next

    return jsonify({'merged_list': result})

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

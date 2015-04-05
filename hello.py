import os
import wingbat 
import json
from flask import Flask

app = Flask(__name__)


myArray = []

for i in range(0, 10):
    myArray.append(wingbat.rgbObject(25*i, 25*i, 25*i))


@app.route('/rgb/')
def printArray():
    counter = 0
    myString = ""
    for myObject in myArray:
        counter = counter+1
        print myArray
        myString = myString + json.dumps(myObject.serialize())
    return myString


@app.route('/')
def hello():
    return 'Hello World!'

@app.route('/color2/<int:color_id>')
def colorMon(color_id):
		if color_id == 16449536:
			return 'red'
		elif color_id == 65280:
			return 'green'
		else:
			return 'yamon'

@app.route('/cooco/<int:red>-<int:green>-<int:blue>')
def RGB(red, green, blue):
    return str(red) + ", " + str(green) + ", " + str(blue)

if __name__=='__main__':
	app.run(debug=True)


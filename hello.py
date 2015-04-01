import os
import wingbat 
import json
from flask import Flask

app = Flask(__name__)



x=wingbat.cRizzleNizPop(25,5,8)
@app.route('/rgb/')
def bob():
	return json.dumps(x.serialize()) #wingbat.cRizzleNizPop(155,11,60)

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

	#sdkjjbd
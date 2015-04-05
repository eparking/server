#!/venv/bin/python
import os
import json
from flask import Flask

print "hello"
app = Flask(__name__)

class RGBAPixel:
	def __init__(self,red,green,blue):
		self.red=red
		self.green=green
		self.blue=blue
	def serialize(self):
		return {"red":self.red,
				"green":self.green,
				"blue":self.blue}

class ParkingSpace:
	def __init__(self,id,vacant):
		self.id=id
		self.vacant=vacant	
	def serialize(self):
		return {
			"id":self.id,
			"vacant":self.vacant
		}

arr=[]

for i in range(0, 10):
    arr.append(ParkingSpace(i, i%2==0))

@app.route('/')
def hello():
	return 'Hello World!'

@app.route('/rgb/')
def printArray():
    counter = 0
    myString = ""
    for RGBAPixel in arr:
        counter = counter+1
        print arr
        myString = myString + json.dumps(RGBAPixel.serialize())
    return myString

@app.route('/color2/<int:color_id>')
def colorMon(color_id):
		if color_id == 16449536:
			return 'red'
		elif color_id == 65280:
			return 'green'
		else:
			return 'yamon'

@app.route('/cooco/<int:red>-<int:green>-<int:blue>')
def cocoo(red, green, blue):
    return str(red) + ", " + str(green) + ", " + str(blue)





@app.route('/create/<int:red>-<int:green>-<int:blue>')
def RGB(red, green,blue):
	create_obj=RGBAPixel(red,green,blue)
	arr.append(create_obj)
	return """<html>
<body>
Added color:
"""+str(red)+", "+str(green)+", "+str(blue)+" at index "+str(len(arr)-1)+"""
</body>
</html>
"""

@app.route('/read/<int:num>')
def read(num):
	if (num>=len(arr)):
			return "invalid index"
	read_obj=arr[num]
	return json.dumps(read_obj.serialize())

@app.route('/update/<int:red>-<int:green>-<int:blue>-<int:num>')
def update(red, green,blue,num):
	if(num>=len(arr)):
		return "invalid index"
	old_obj=arr[num]
	old_obj.red=red
	old_obj.green=green
	old_obj.blue=blue
	return """<html>
<body>
Updated color:
"""+str(red)+", "+str(green)+", "+str(blue)+" at index "+str(num)+"""
</body>
</html>
"""


@app.route('/delete/<int:num>')
def delete(num):
	if(num>=len(arr)):
		return "invalid index"
	
	arr.pop(num)

	return "asad"


if __name__=='__main__':
	app.run(debug=True)
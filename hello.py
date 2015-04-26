#!/venv/bin/python
import os
import json
import sqlite3
from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
import datetime

print "hello"
app = Flask(__name__)
app.config.from_object('config')
db = SQLAlchemy(app)

#models.py file
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nickname = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    spots = db.relationship('Spot', backref='author', lazy='dynamic')

    def __repr__(self):
        return '<User %r>' % (self.nickname)

class Spot(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    location = db.Column(db.String(140))
    timestamp = db.Column(db.DateTime)
    vacancy = db.Column(db.Integer)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __repr__(self):
        return '<Spot %r>' % (self.location)
#end models.py file

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





@app.route('/create/<int:id>-<string:vacant>')
def RGB(id,vacant):
	create_obj=ParkingSpace(id,vacant)
	arr.append(create_obj)
	return """<html>
<body>
Added ParkingSpace:
"""+"id: "+str(id)+", vacant: "+vacant+" at index "+str(len(arr)-1)+"""
</body>
</html>
"""

@app.route('/read/<int:num>')
def read(num):
	if (num>=len(arr)):
			return "invalid index"
	read_obj=arr[num]
	return json.dumps(read_obj.serialize())

@app.route('/update/<int:id>-<string:vacant>-<int:num>')
def update(id,vacant,num):
	if(num>=len(arr)):
		return "invalid index"
	old_obj=arr[num]
	old_obj.id=id
	if vacant == 'True':
		old_obj.vacant=True
	elif vacant == 'False':
		old_obj.vacant=False
	return """<html>
<body>
Updated:
"""+" id: "+str(id)+", vacant: "+vacant+ " at index "+str(num)+"""
</body>
</html>
"""


@app.route('/delete/<int:num>')
def delete(num):
	if(num>=len(arr)):
		return "invalid index"
	
	arr.pop(num)

	return "asad"

@app.route('/showArr')
def show():
    arrList = ""
    for i in arr:
        arrList += "id:" + arr[i].id + " Vacant:" + arr[i].vacant + ".........." 
    return arrList

############################################
#              Database Stuff              #

#Sources: http://www.blog.pythonlibrary.org/2012/07/18/python-a-simple-step-by-step-sqlite-tutorial/
#Sources: https://www.youtube.com/watch?v=n-Rtfd1Vv_M

#Current Problem: when try to use route to add to db, "SQLite objects created in a thread can only be used in that same thread"
conn = sqlite3.connect("mydatabase.db")
cursor = conn.cursor()

# create a table
#Boolean values are stored as integers 0 (false) and 1 (true).
#cursor.execute("""CREATE TABLE parkingspots
#						time integer) 
#				""")

@app.route('/create_user/<string:n_name>-<string:e_mail>')#create obj in db
def makeUser(n_name,e_mail):
	u = User(nickname=n_name, email=e_mail)
	db.session.add(u)
	db.session.commit()
	return """<html>
<body>
Added ParkingSpace:
"""+ "_" + "User Added!" +"_" +"""
</body>
</html>
"""

@app.route('/create_db/<int:id>-<int:vacant>-<string:location>-<int:time>')#create obj in db
def makeSpot(id,vacant,location,time):
	u = User.query.get(id)
	p = Spot(location=location, timestamp=datetime.datetime.utcnow(), vacancy=vacant, author=u)
	db.session.add(p)
	db.session.commit()
	return """<html>
<body>
Added ParkingSpace:
"""+ "_" + "Nice try!" +"_" +"""
</body>
</html>
"""



if __name__=='__main__':
	app.run(debug=True)
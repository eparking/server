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
# User Properties: name, email, spots(relationship), id
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nickname = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    spots = db.relationship('Spot', backref='author', lazy='dynamic')

    def __repr__(self):
        return '<User %r>' % (self.nickname)

# Spot Properties: location(string), timestamp(DateTime), vacancy(Integer), user's id(Integer), id (include time amount?)
class Spot(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    location = db.Column(db.String(140))
    timestamp = db.Column(db.DateTime)
    vacancy = db.Column(db.Integer)
    owner_id = db.Column(db.Integer)
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

# Need to...
# Add time to ?
# check time/count down
# View spots and their status (who has them, how much time)

@app.route('/create_user/<string:n_name>-<string:e_mail>')#create obj in db
def createUser(n_name,e_mail):
	u = User(nickname=n_name, email=e_mail) #send email when time is almost up?....change to phone number?
	db.session.add(u)
	db.session.commit()
	return """<html>
<body>
Added ParkingSpace:
"""+ "_" + "User Added!" +"_" +"""
</body>
</html>
"""
@app.route('/create_spot/<int:owner>-<string:location>')
def createSpot(owner,location):
	p = Spot(owner_id=owner, location=location, timestamp=datetime.datetime.utcnow(), vacancy=0)
	db.session.add(p)
	db.session.commit()
	return """<html>
<body>
Added ParkingSpace:
"""+ "_" + "Spot Created!" +"_" +"""
</body>
</html>
"""

@app.route('/take_spot/<int:user_id>-<int:location_id>-<int:time>')
def takeSpot(user_id,location_id,time):
	user = User.query.get(user_id)
	location = Spot.query.get(location_id)
	location.timestamp = datetime.datetime.utcnow()
	location.vacancy = 1
	location.user_id = user.id
	db.session.commit()
	return """<html>
<body>
Added ParkingSpace:
"""+ "_" + "Spot Taken!" +"_" +"""
</body>
</html>
"""

@app.route('/drop_spot/<int:location_id>')
def dropSpot(location_id):
	location = Spot.query.get(location_id)
	location.vacancy = 0
	db.session.commit()
	return """<html>
<body>
Added ParkingSpace:
"""+ "_" + "Spot dropped!" +"_" +"""
</body>
</html>
"""

@app.route('/view_lot/')
def viewlot():
	lot = ''
	spots=Spot.query.all()
	for s in spots:
		u = Spot.query.get(s.id)
		lot+=('||Location ID: ')
		lot+=(str(u.id))
		lot+=('||')
		lot+=('...Location: ')
		lot+=(str(u.location))
		lot+=('...Vacancy: ')
		lot+=(str(u.vacancy))
		lot+=('...User-Id: ')
		lot+=(str(u.user_id))
		lot+=('...Owner-Id: ')
		lot+=(str(u.owner_id))

	return """<html>
<body>
"""+ "_" + lot +"_" +"""
</body>
</html>
"""



if __name__=='__main__':
	app.run(debug=True)
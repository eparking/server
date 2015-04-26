import sqlite3
import os
import json
import sqlite3
from flask import g
from flask import Flask

DATABASE =  'Users\user\Documents\github\practice_db.db'

app = Flask(__name__)
app.config.from_object(__name__)

def connect_db():
	return sqlite3.connect(app.config['DATABASE'])

@app.route('/test_db')
def test():
	g.db = connect_db()	
	cur = g.db.execute('select id, time from pSpaces')
	spaces = [dict(id=row[0], amount=row[1]) for row in cur.fetchall()]
	g.db.close()
	return spaces

@app.route('/')
def hello():
	return 'Hello World!'

#def main(): 
	#conn = sqlite3.connect("mydatabase.db") # or use :memory: to put it in RAM
 
	cursor = conn.cursor()

@app.route('/create_db/<int:id>-<string:vacant>-<string:location>-<int:time>')#create obj in db
def makeSpot(id,vacant,location,time):
	g.db.execute('INSERT INTO parkingspots VALUES (id, vacant, location, time') 
	conn.commit()
	return """<html>
<body>
Added ParkingSpace:
"""+ "_" + "Nice try!" +"_" +"""
</body>
</html>
"""

# create a table
#Boolean values are stored as integers 0 (false) and 1 (true).
	cursor.execute("""CREATE TABLE parkingspots
						(id integer, vacant integer, location text, 
						time integer) 
					""")
 #insert some data
#probably use this line alot..
	cursor.execute("INSERT INTO parkingspots VALUES (0, 1, 'georgia', 20)")
 
# save data to database
	conn.commit()
 
# insert multiple records using the more secure "?" method
	parkingspots = [(0, 1, 'georgia', 20),
	          (1, 0, 'filly', 10),
	          (2, 1, 'bama', 100),
	          (3, 0, 'illestnoy', 0)]
	cursor.executemany("INSERT INTO parkingspots VALUES (?,?,?,?)", parkingspots)
	conn.commit()

#updating stuff in db
	sql = """
	UPDATE parkingspots 
	SET time = 20 
	WHERE time = 0
	"""
	cursor.execute(sql)
	conn.commit()

	#deleting stuff from db 
	sql = """
	DELETE FROM parkingspots
	WHERE id = 0
	"""
	cursor.execute(sql)
	conn.commit()

	for row in cursor:
		print(row)

if __name__=='__main__':
	app.run(debug=True)
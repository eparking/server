import sqlite3

def main(): 
	conn = sqlite3.connect("mydatabase.db") # or use :memory: to put it in RAM
 
	cursor = conn.cursor()
 
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

	if __name__=='__main__':main()
		#app.run(debug=True)
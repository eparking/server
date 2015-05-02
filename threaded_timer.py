import thread, threading
import time

def runTime(amountOfTime):
		time.sleep(10)
		print "time is up"

t = threading.Thread(target=runTime, args=())
t.daemon=True
#t.start()

runTime(5)

for i in range(1,10):
	print i


mystuff = {'chikn_plz': "yuh want freyes wit dat son?"}
print mystuff['chikn_plz']

def zorro():
	print ""

class cRizzleNizPop(object):
#    def rgb():
#        rgb=__init__()
    def __init__(self,red,green,blue):
        self.r=red
        self.g=green
        self.b=blue

    def serialize(self):
    	return {"red":self.r,
    			"green":self.g,
    			"blue":self.b}




class rgbObject(object):
#    def rgb():
#        rgb=__init__()
    def __init__(self,red,green,blue):
        self.r=red
        print self.r
        self.g=green
        self.b=blue

    def serialize(self):
    	return {"red":self.r,
    			"green":self.g,
    			"blue":self.b}

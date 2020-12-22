class Dummy:
    def __init__(self, x):
        self.x = x
    
    @property
    def xValue(self):
        return self.x

    @xValue.setter
    def xValue(self,value):
        self.x = value

d=Dummy(17)
print(d.x)
# 1
d.xValue = 20
print(d.x)
# 2
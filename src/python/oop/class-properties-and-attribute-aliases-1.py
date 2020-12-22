class Dummy:
    def __init__(self, x):
        self._x = x

    @property
    def x(self):
        return self._x

    @x.setter
    def x(self, inp):
        self._x = inp

    @x.deleter
    def x(self):
        del self._x

    # Alias
    xValue = x

d = Dummy(17)
print(d.x, d.xValue)
#=> (17, 17)
d.x = 0
print(d.x, d.xValue)
#=> (0, 0)
d.xValue = 100
print(d.x, d.xValue)
#=> (100, 100)

r = Dummy(34)
print(d.xValue)
print(r.xValue)
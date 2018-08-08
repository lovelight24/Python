import math
class Circle:
    def __init__(self, width):
        self.__wid = width

    def setWidth(self, width):
           self.__wid = width

    def getWidth(self):
        return self.__wid

    def area(self):
        return math.pi * self.__wid**2

    def __mul__(self, other_Circle):
        return  Circle(self.__wid - other_Circle.__wid)

a = Circle(4)
print(a.getWidth())

b = Circle(5)
print(b.getWidth())

c = a * b
print(c.getWidth())


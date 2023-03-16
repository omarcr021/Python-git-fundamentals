class Point():
    def __init__(self,input1,input2):
        self.x = input1
        self.y = input2

xV = int(input("Insert x value: "))
y = int(input("Insert y value: "))

p = Point(xV,y)
print(p.x)
print(p.y)
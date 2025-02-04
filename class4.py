import math

class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
    def show(self):
        print(f"Point coordinates: ({self.x}, {self.y})")
    def move(self, new_x, new_y):
        self.x = new_x
        self.y = new_y
    def dist(self, other_point):
        print(math.sqrt((self.x - other_point.x) ** 2 + (self.y - other_point.y) ** 2))

x1=int(input())
y1=int(input())
x2=int(input())
y2=int(input())
p1=Point(x1,y1)
p2=Point(x2,y2)

p1.show() 

p1.dist(p2)

p1.move(10, 15)
p1.show() 
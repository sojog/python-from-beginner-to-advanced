import math
from typing import Self

class Point:
    def __init__(self, x:int, y:int):
        self.coord_x = x
        self.coord_y = y

    def __str__(self) -> str:
        return f"x = {self.coord_x}, y = {self.coord_y}"
    
    def show(self):
        print(self)

    def move(self, new_x:int, new_y:int):
        self.coord_x = new_x
        self.coord_y = new_y

    def set_to_origin(self):
        self.move(0, 0)

    def dist(self, other:Self):
        return (math.sqrt((self.coord_x - other.coord_x)**2 + (self.coord_y - other.coord_y)**2))

p1 = Point(10, 20)
print(p1)
p1.show()
p1.move(40, 50)
p1.show()
p1.set_to_origin()
p1.show()
p2 = Point(10, 10)
print(p1.dist(p2))
print(p2.dist(p1))


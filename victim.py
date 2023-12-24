import turtle
from random import randint
class Victim:
    turtle.pu()
    turtle.speed(10)
    def new_point(self,width,hight):
        turtle.setpos(randint(-width,width),randint(-hight,hight))
        # turtle.setpos(400,randint(-hight,hight))
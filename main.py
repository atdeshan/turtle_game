from turtle import Turtle,Screen
from snake_brain import Brain
from victim import Victim

brain = Brain()
victi = Victim()
screen = brain.screen

screen.listen()
screen_width = 500
screen_hight = 500
screen.setup(width=screen_width,height=screen_hight)
brain.add_turtle_into_end()
brain.add_turtle_into_end()
brain.add_turtle_into_end()
screen.onkey(fun=brain.go_forward,key="space")
screen.onkey(fun=brain.turn_left,key="Left")
screen.onkey(fun=brain.turn_right,key="Right")
screen.onkey(fun=brain.up,key="Up")
screen.onkey(fun=brain.down,key="Down")

victi.new_point(int(screen_width/2),int(screen_hight/2))
screen.exitonclick()


from turtle import Turtle,Screen
import time


class Brain:
    screen = Screen()
    turtle_list = []
    x_y_coordinates = []
    
    
    def add_turtle_into_end(self):
        jam = Turtle()
        self.turtle_list.append(jam)
        self.turtle_list[len(self.turtle_list)-1].pu()
        self.turtle_list[len(self.turtle_list)-1].pensize(4)
        self.turtle_list[len(self.turtle_list)-1].shape("square")
        self.turtle_list[len(self.turtle_list)-1].speed(.6)


        

    # def extend_turtle(self):
    #     x = 15
    #     for i in range(0,len(self.turtle_list)):
    #         self.turtle_list[i].setposition(x-15,0)
    #         x-=15

   
    
    def go_forward(self):
        
        time.sleep(.3) 
        for i in self.turtle_list:
            self.x_y_coordinates.append( i.position())
        self.screen.tracer(0)
        self.turtle_list[0].forward(20)
        for i in range(1,len(self.turtle_list)):
            self.turtle_list[i].goto(self.x_y_coordinates[i-1])
            
        self.x_y_coordinates.clear()
        self.screen.update()
        
        self.go_forward()

            
            
    # movememts
    def turn_left(self):
        angle = self.turtle_list[0].heading()
        if angle==90:
            self.turtle_list[0].left(90)
        elif angle==270:
            self.turtle_list[0].right(90)

    def turn_right(self):
        angle = self.turtle_list[0].heading()
        if angle==90:
            self.turtle_list[0].right(90)
        elif angle==270:
            self.turtle_list[0].left(90)
    def up(self):
        angle = self.turtle_list[0].heading()
        if angle == 0 :
            self.turtle_list[0].left(90)
        elif angle == 180:
            self.turtle_list[0].right(90)
    def down(self):
        angle = self.turtle_list[0].heading()
        if angle == 0 :
            self.turtle_list[0].right(90)
        elif angle == 180:
            self.turtle_list[0].left(90)

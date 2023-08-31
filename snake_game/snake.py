from turtle import Turtle,Screen
POSITIONS = [(0,0),(-20,0),(-40,0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
RIGHT = 0
LEFT = 180

class Snake:
   
    def __init__(self):
        #list of snake body segments created
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]
        
    #creating snake body using 3 squares    
    def create_snake(self):    
        for position in POSITIONS:
            self.add_segment(position)
           
    def add_segment(self,position):
        new_section = Turtle("square")
        new_section.color("white")
        new_section.penup()
        new_section.goto(position)
        self.segments.append(new_section)

    def extend_snake(self):
        self.add_segment(self.segments[-1].position())


    def move(self):
        #for moving the snake
        for seg_num in range(len(self.segments)-1,0,-1):  #range(start=length of segment list -1,stop=0,step=-1)
            new_x =self.segments[seg_num-1].xcor()
            new_y = self.segments[seg_num-1].ycor()
            self.segments[seg_num].goto(new_x,new_y)
        self.head.forward(MOVE_DISTANCE)

    def snake_reset(self):
        for seg in self.segments:
            seg.goto(1000,1000)
        self.segments.clear()
        self.create_snake()
        self.head = self.segments[0]

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(90)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(270)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(0)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(180)

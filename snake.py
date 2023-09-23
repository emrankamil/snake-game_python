from turtle import Turtle
STARTING_POSITION=[(0,0),(-20,0),(-40,0)]
MOVE_DISTANCE=10
DIRECTION=[0,90,180,270]



class Snake():
    def __init__(self):
        
        self.segments=[]
        
        for i in STARTING_POSITION:
            self.add_segment(i)
            
        self.head=self.segments[0]

    def add_segment(self,position):
        new_segment= Turtle("square")
        new_segment.color("white")
        new_segment.speed("fast")
        new_segment.penup()
        new_segment.goto(position)
        segments=self.segments
        segments.append(new_segment)

    def extende(self):
        self.add_segment(self.segments[-1].position())



    def move(self):
        for seg_num in range(len(self.segments)-1,0,-1):
            new_x=self.segments[seg_num-1].xcor()
            new_y=self.segments[seg_num-1].ycor()
            self.segments[seg_num].goto(new_x,new_y)
        self.head.fd(MOVE_DISTANCE)
        

    def up(self):
        if self.head.heading()!=270:
            self.head.setheading(90)
    def right(self):
        if self.head.heading()!=180:
            self.head.setheading(0)
    def left(self):
        if self.head.heading()!=0:
            self.head.setheading(180)
    def down(self):
        if self.head.heading()!=90:
            self.head.setheading(270)





    




        


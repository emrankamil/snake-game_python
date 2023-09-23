from turtle import Turtle
import time

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score=0

    def count(self):
        self.color("white")
        self.ht()
        self.penup()
        self.setposition(0,265)
        self.write(f"score: {self.score}",False,"center",("Courier",24,"normal"))
    
    def refresh(self):
        self.clear()

    def gameover(self):
        self.color("red")
        self.goto(0,0)
        self.write(f"GAME OVER! ",False,"center",("Courier",34,"normal"))
            
            


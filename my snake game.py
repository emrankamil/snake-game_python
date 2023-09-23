from turtle import Screen
from snake import Snake
import time
from food import Food
from scoreboard import Score

screen=Screen()
screen.setup(600,600)
screen.bgcolor("black")
screen.title("snake game")
screen.listen()
screen.tracer(0)

snake=Snake()
food=Food()
score=Score()


screen.onkey(key="Up",fun=snake.up)
screen.onkey(key="Down",fun=snake.down)
screen.onkey(key="Right",fun=snake.right)
screen.onkey(key="Left",fun=snake.left)

game_is_on=True

while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()
    score.count()

    if snake.head.distance(food) < 15:
        score.score+=1
        snake.extende()
        food.refresh()
        score.refresh()

    if abs(snake.head.xcor())>=290 or abs(snake.head.ycor())>=290:
        score.gameover()
        game_is_on=False
    
    for seg in snake.segments[1:]:
        if seg.distance(snake.head)< 2:
            score.gameover()
            game_is_on=False


        

        

    



screen.exitonclick()

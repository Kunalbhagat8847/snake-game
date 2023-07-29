import turtle
from turtle import Turtle,Screen
from Snake import Snake
from Food import Food
from scoreboard import ScoreBoard
import time
screen=Screen()
screen.setup(width=600,height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

snake=Snake()
food=Food()
scoreboard=ScoreBoard()



screen.listen()
screen.onkey(snake.up ,"Up")
screen.onkey(snake.down ,"Down")
screen.onkey(snake.left ,"Left")
screen.onkey(snake.right ,"Right")


game_on=True
while game_on:
    screen.update()
    time.sleep(0.1)
    snake.move()
# Detect colliding with food
    if snake.head.distance(food)<13:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()

# Detect collision with wall
    if snake.head.xcor()>280 or snake.head.xcor()< -285 or snake.head.ycor()>285 or snake.head.ycor()<-285:
        scoreboard.reset()
        snake.reset()

    for segment in snake.segment[1:]:
        if snake.head.distance(segment)<10:
            scoreboard.reset()
            snake.reset()


screen.exitonclick()

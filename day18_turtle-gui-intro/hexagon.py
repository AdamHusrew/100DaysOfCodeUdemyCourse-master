from turtle import Turtle, Screen

timmy_the_turtle = Turtle()
timmy_the_turtle.shape("turtle")
timmy_the_turtle.color("red2")

for i in range(0, 6):
    timmy_the_turtle.forward(100)
    timmy_the_turtle.right(60)

screen = Screen()
screen.exitonclick()



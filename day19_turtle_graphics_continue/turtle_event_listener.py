from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()


def move_up():
    if tim.heading() != 90.0:
        tim.setheading(90)
    tim.forward(10)


def move_down():
    if tim.heading() != 270.0:
        tim.setheading(270)
    tim.forward(10)


def turn_right():
    if tim.heading() != 0.0:
        tim.setheading(0)
    tim.forward(10)


def turn_left():
    if tim.heading() != 180.0:
        tim.setheading(180)
    tim.forward(10)


def clear():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()


screen.listen()
screen.onkey(move_up, "w")
screen.onkey(move_down, "s")
screen.onkey(turn_right, "d")
screen.onkey(turn_left, "a")
screen.onkey(clear, "c")
screen.onkey(tim.home, "h")

screen.exitonclick()

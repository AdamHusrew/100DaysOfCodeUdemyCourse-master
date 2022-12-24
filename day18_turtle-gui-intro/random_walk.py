import random
from turtle import Turtle, Screen

tim = Turtle()
tim.shape("arrow")
colors = ["yellow", "gold", "orange", "red", "maroon", "violet", "magenta", "purple", "navy", "blue", "skyblue", "cyan",
          "turquoise", "lightgreen", "green", "darkgreen", "chocolate", "brown", "black", "gray"]

tim.speed(0)
directions = [0, 90, 180, 270]
tim.pensize(10)


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    result = (r, g, b)
    return result


for _ in range(200):
    tim.forward(30)
    tim.setheading(random.choice(directions))
    tim.color(random.choice(colors))

screen = Screen()
screen.exitonclick()

import random
from turtle import Turtle, Screen

tim = Turtle()
tim.shape("arrow")
colors = ["yellow", "gold", "orange", "red", "maroon", "violet", "magenta", "purple", "navy", "blue", "skyblue", "cyan",
          "turquoise", "lightgreen", "green", "darkgreen", "chocolate", "brown", "black", "gray"]

tim.speed(0)
directions = [0, 90, 180, 270]
tim.pensize(1)

def draw_spiregraph(size_of_gap):
    for _ in range(int(360/size_of_gap)):
        tim.circle(100)
        current_heading = tim.heading()
        tim.setheading(current_heading+ size_of_gap)
        tim.color(random.choice(colors))

draw_spiregraph(5)

screen = Screen()
screen.exitonclick()

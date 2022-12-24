from turtle import Turtle, Screen

tim = Turtle()
tim.shape("arrow")
colors = ["yellow", "gold", "orange", "red", "maroon", "violet", "magenta", "purple", "navy", "blue", "skyblue", "cyan",
          "turquoise", "lightgreen", "green", "darkgreen", "chocolate", "brown", "black", "gray"]
tim.speed(10)
tim.pensize(5)

tim.resizemode("auto")


def draw_shape(num_sides):
    for i in range(num_sides):
        angle = 360 / num_sides
        tim.forward(60)
        tim.right(angle)


for i in range(3, 100, 1):
    draw_shape(i)
    tim.color(colors[i % len(colors)])
screen = Screen()
screen.exitonclick()

import math


def paint_calc(height, width, cover):
    area = height * width
    number_of_cans = math.ceil(area / cover)
    print(f"You will need {number_of_cans} to paint.")


height = int(input("Height of wall: "))
width = int(input("Width of wall: "))
coverage = 5

paint_calc(height=height, width=width, cover=coverage)

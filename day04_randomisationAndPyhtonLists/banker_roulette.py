import random

names_string = input("Give me everybody's names, seperated by a comma: ")
names = names_string.split(",")

print(names)

num_items = len(names)
print(names[random.randint(0, num_items-1)])

print("-------------random.choice-----------")

print(random.choice(names))
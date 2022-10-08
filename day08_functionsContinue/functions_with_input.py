def greet():
    print("Hello")
    print("How do you do?")
    print("Isn't it the weather nice today?")


print("----------------------------------")
greet()


def greet2(name):
    print(f"Hello {name}")
    print(f"How do you do {name}?")


print("----------------------------------")
greet2("Adam")


def greet3(name, location):
    print(f"Hello {name}")
    print(f"What is it like in {location}?")


print("----------------------------------")
greet3("Adam", "Ankara")

print("----------------------------------")
greet3(name="Mike", location="London")

print("----------------------------------")
greet3(location="London", name="Mike")

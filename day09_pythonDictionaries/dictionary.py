# Creating a dictionary
programming_dictionary = {"Bug": "An error in a program that prevents the program from running as expected.",
                          "Function": "A piece of code that you can easily call over and over again."}
print("----------------------------")
print(programming_dictionary)

# Adding elements to dictionary
programming_dictionary["Loop"] = "The action of doing something";
print("----------------------------")
print(programming_dictionary)

# Wiping th dictionary
# programming_dictionary = {}
# print("----------------------------")
# print(programming_dictionary)

# Creating an empty dict
empty_dictionary = {}

# Edit an item in a dictionary
programming_dictionary["Loop"] = ""
print("----------------------------")
print(programming_dictionary)


for key in programming_dictionary:
    print(key + " : " + programming_dictionary[key])


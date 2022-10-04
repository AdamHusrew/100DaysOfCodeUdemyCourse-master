import random
import string

letters = []
for i in string.ascii_letters:
    letters.append(str(i))
# print(letters)

numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
# print(numbers)

symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+', '_']
# print(symbols)


print("Welcome to password generator")

nr_letters = int(input("How many letters would you like in your password?\n"))
nr_numbers = int(input("How many numbers would you like in your password?\n"))
nr_symbols = int(input("How many symbols would you like in your password?\n"))

password = []

for char in range(1, nr_letters + 1):
    random_char = letters[(random.randint(0, len(letters) + 1) % len(letters))]
    password += random_char

# print(password)

for char in range(1, nr_numbers + 1):
    random_char = numbers[(random.randint(0, len(numbers) + 1) % len(numbers))]
    password += random_char

# print(password)

for char in range(1, nr_symbols + 1):
    random_char = symbols[(random.randint(0, len(symbols) + 1) % len(symbols))]
    password += random_char

print(password)

random.shuffle(password)

print(password)

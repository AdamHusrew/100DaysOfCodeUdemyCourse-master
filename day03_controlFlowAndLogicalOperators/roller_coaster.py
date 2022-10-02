print("Welcome to the Roller Coaster!")
height = int(input("What is your height in cm?\n"))
bill = 0
if height > 120:
    print("You can ride the roller coaster!")
    age = int(input("What is your age?\n"))
    if age < 12:
        print("Child tickets are $5.")
        bill = 5
    elif age <= 18:
        print("Youth tickets are $7")
        bill = 7
    else:
        print("Adult tickets are $12")
        bill = 12

    wants_photo = input("Do you want a photo taken ? (Y/N)")
    if wants_photo == "Y" or wants_photo == "y":
        bill += 3

    print(f"Your final bill is {bill}")

else:
    print("You cannot ride the roller coaster!")

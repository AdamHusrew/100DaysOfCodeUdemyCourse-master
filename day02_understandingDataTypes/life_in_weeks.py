# LÄ°fe in Weeks


# ð¨ Don't change the code below ð
age = input("What is your current age? ")
# ð¨ Don't change the code above ð

# Write your code below this line ð

age_as_int = int(age)

years_remaining = 80 - age_as_int
days_remaining = years_remaining * 365
weeks_remaining = years_remaining * 52
months_remaining = years_remaining * 12

print(f"You have {days_remaining} days, {weeks_remaining} weeks, {months_remaining} months. ")

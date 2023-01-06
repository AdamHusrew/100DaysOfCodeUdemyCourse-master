# TODO: Create a letter using starting_letter.txt
# for each name in invited_names.txt
# Replace the [name] placeholder with the actual name.
# Save the letters in the folder "ReadyToSend".

# Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
# Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
# Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

letter_content = ""
names = []
line = ""

with open("Input/Names/invited_names.txt") as file:
    names = file.read().split("\n")

for name in names:
    with open("Input/Letters/starting_letter.txt", mode="r") as file:
        letter_content = file.read()
        letter_content = letter_content.replace("[name]", name)
        letter_name = name + ".txt"
        with open("Output/ReadyToSend/" + letter_name, mode="w") as letter:
            letter.write(letter_content)

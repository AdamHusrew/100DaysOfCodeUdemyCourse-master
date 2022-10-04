students_heights = input("Input a list of students height: ").split()

for n in range(0, len(students_heights)):
    students_heights[n] = int(students_heights[n])
print(students_heights)

total_height = 0
for n in range(0, len(students_heights)):
    total_height += students_heights[n]

num_of_students = len(students_heights)

average_height = round(total_height / num_of_students)
print(f"Sum: {sum(students_heights)}")
print(f"Max: {max(students_heights)}")
print(f"Min: {min(students_heights)}")
print(f"Total height: {total_height}")
print(f"Average height: {average_height}")

# Calculate the average height of the students, without using the function len () and sum ()

# 🚨 Don't change the code below 👇
student_heights = input("Enter a list of the students' heights in cm separated only by space ").split()
for n in range(0, len(student_heights)):
    student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆


# Write your code below this row 👇
suma = 0
for height in student_heights:
    suma = suma + height

# print(suma)

N = 0
for height in student_heights:
    N = N + 1

# print(N)
Average_height = round(suma / N)
print(f"The average height is {Average_height}cm.") 
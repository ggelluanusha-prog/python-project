name = "Anusha"
marks = [78, 85, 69, 90, 88]

total = sum(marks)
percentage = total / len(marks)

if percentage >= 75:
    grade = "Distinction"
elif percentage >= 60:
    grade = "First Class"
elif percentage >= 50:
    grade = "Second Class"
else:
    grade = "Fail"

print("Student Name:", name)
print("Total Marks:", total)
print("Percentage:", percentage)
print("Result:", grade)

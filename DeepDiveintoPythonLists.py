#Question 4 Task 1
students = ["John", "Doe", "Jane", "Smith"]
grades = [85, 90, 78, 88]
activities = ["Football", "Music", "Art", "Dance"]

for i in grades:
    if i < 80:
        index = grades.index(i)
print(index)

print(students[2], grades[2], activities[2])

#Question 4 Task 2 
students.remove(students[index])
students_approved = students
print(students_approved) #Task 3

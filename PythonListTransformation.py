#Question 1 Task 1
grades = [85, 90, 78, 88, 76, 95, 89, 80, 72, 93]
grades.sort()
grades.reverse()
print(grades)

#Question 1 Task 2
length_grades=len(grades)
total=sum(grades)
average_grades = total / length_grades

print(average_grades)

#Question 1 Task 3

if grades[-1] < 80:
    grades[-1] = "Failed"
if grades[-2] < 80:
    grades[-2] = "Failed"
if grades[-3] < 80:
    grades[-3] = "Failed"
if grades[-4] < 80:
    grades[-4] = "Failed"
if grades[-5] < 80:
    grades[-5] = "Failed"
if grades[-6] < 80:
    grades[-6] = "Failed"
if grades[-7] < 80:
    grades[-7] = "Failed"
if grades[-8] < 80:
    grades[-8] = "Failed"
if grades[-9] < 80:
    grades[-9] = "Failed"  
if grades[-10] < 80:
    grades[-10] = "Failed"  

print(grades)
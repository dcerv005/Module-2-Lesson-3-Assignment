#Question 3 Task 1

temperatures = [72, 75, 78, 79, 80, 81, 82, 83, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106]
second_week = temperatures[7:14]

print(second_week)
#Question 3 Task 2
list=[]
for i in temperatures:
    if i >= 100:
        list.append(i)
    else:
        pass
print(list)

#Question 3 Task 3

temperatures.reverse()
print(temperatures[4:10])
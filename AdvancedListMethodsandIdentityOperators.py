#Question 2 Task 1
submitted = ["Alice", "Bob", "Charlie", "David"]
attended = ["Charlie", "Eve", "Alice", "Frank"]

full_list = submitted + attended
print(full_list)

both =[]


if full_list.count(submitted[0]) > 1:
    both.append(submitted[0])
if full_list.count(submitted[1]) > 1:
    both.append(submitted[1])
if full_list.count(submitted[2]) > 1:
    both.append(submitted[2])
if full_list.count(submitted[3]) > 1:
    both.append(submitted[3])

print("The list of students that submitted their assigments and attended class are: ", both)

#Question 2 Task 2
submitted.sort()
attended.sort()
if submitted is attended:
    print("Lists are the same")
else:
    print("Lists are different")

#Question 2 Task 3
submitted = ["Alice", "Bob", "Charlie", "David"]
attended = ["Charlie", "Eve", "Alice", "Frank"]
new_list=[]
if attended[0] in submitted:
    new_list.append(attended[0])
else:
    pass
if attended[1] in submitted:
    new_list.append(attended[1])
else:
    pass
if attended[2] in submitted:
    new_list.append(attended[2])
else:
    pass
if attended[3] in submitted:
    new_list.append(attended[3])
else:
    pass

print(new_list)

# list comprehension =  a way to create a new list with less syntax
#                       can mimic certain lambda functions, easier to read
#                       list = [expression for item in iterable]
#                       list = [expression for item in iterable if conditional]
#                       list = [expression if/else for item in iterable]
# --------------------------------------------------------------

print("----------------")
squares = []                # create an empty list
for i in range(1,11):       # create a for loop
    squares.append(i * i)    # define what each loop iteration should do
print(squares)
print("----------------")
squares2 = [i * i for i in range(1,11)]
print(squares2)
print("----------------")
students = [100,90,80,70,60,50,40,30,0]

passed_students = list(filter(lambda x: x >= 60, students))

print(passed_students)
print("----------------")
passed_students2 = [i for i in students if i >= 60]
passed_students3 = [i if i >= 60 else "FAILED" for i in students ]

print(passed_students2)
print("----------------")
print(passed_students3)
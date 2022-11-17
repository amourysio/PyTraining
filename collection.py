# Collection = single "variable" used to store multiple values
#   List = [] ordered and changeable, Duplicates Ok
#   Set = {} unordered and immutable, but Add/Remove Ok. No Duplicates
#   Tuple = () ordered and unchangeable. Duplicates Ok. Faster

# List
# fruits = ["apple", "orange", "banana", "coconut"]

# print(dir(fruits))
# print(help(fruits))
# print(len(fruits))
# print("coconut" in fruits)

# fruits[0] = "pineapple"
# fruits.append("pineapple")

# fruits.sort()
# fruits.reverse()
# fruits.clear()
# print(fruits.index("banana"))
# print(fruits.count("banana"))
# print(fruits)

# Set
# WE CANNOT GET THE INDEX OF SET
# is good for constants if you work with colours for example

# fruits = {"apple", "orange", "banana", "coconut"}
# fruits.add("pineapple")
# fruits.remove("apple")
# fruits.pop()
# fruits.clear()
# print(fruits)

# Tuple

fruits = ("apple", "orange", "banana", "coconut")

print(fruits)
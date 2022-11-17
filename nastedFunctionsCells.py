# nested function cells = function inside
# other function cells innermost function cells are resolved
# first returned value is used as argument for the next outer function

# num = input("Enter a whole positive number: ")
# num = float(num)
# num = abs(num)
# num = round(num)
# print(num)

print(round(abs(float(input("Enter a whole positive number: ")))))


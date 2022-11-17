# lambda function = function written in 1 line using lambda keyword
#                   accepts any number of arguments, but only has one expression.
#                   (think of it as a shortcut)
#                   (useful if needed for a short period of time, throw-away)
#
# lambda parameters:expression

double = lambda x: x * 2
multiply = lambda x, y: x * y
add = lambda x, y, z: x + y + z
full_name = lambda first_name, last_name: f"Your name is {first_name} {last_name}"
age_check = lambda age: True if age >= 18 else False


print(double(2))
print(multiply(5,5))
print(add(1,2,3))
print(full_name("Ho", "Se"))
print(age_check(25))

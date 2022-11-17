# function = a block of code which is executed only when it is called.

def hello(first_name, last_name, age):
    print(f"Hello {first_name}, {last_name}, {age}")
    print(f"You are {str(age)}, years old")
    print("Have a nice day!")


hello("Bro", "Code", 21)


def multiply(number1,number2):
    return number1 * number2


print(multiply(6,8))

# key argument


def hi(first,middle,last):
    print(f"Hi {first} {middle} {last}")


print(hi(first="Hussein",middle="Omar",last="Amouri"))
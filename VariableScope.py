# scope = The Region that a variable is recognized

# global scope
name = "Bro"

# LEGB = Local Enclosing GLobal Built-In
# Local scope
def display_name():
    name = "Code"
    print(name)

display_name()
print(name)
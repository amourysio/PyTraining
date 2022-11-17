# exception = events detected during execution that interrupt the flow of a program

try:
    numerator = int(input("Enter a number to divide: "))
    denominator = int(input("Enter a number to divide by: "))
    result = numerator / denominator
except ZeroDivisionError as e:
    print(e)
    print("You can't divide by zero! idiot!")
except ValueError as e:
    print(e)
    print("Enter Only number please!")
except Exception as e:
    print(e)
    print("Something went wrong :(")
else:
    # if there is no Exception
    print(result)
finally:
    # if we open file to close them
    print("This will always execute!")
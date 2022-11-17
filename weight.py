# Python weight converter

weight = float(input("Please enter you weight: "))
unit = input("Kilograms or Pounds? (K or L): ")

if unit == "K" or unit == "k":
    weight = weight * 2.2046
    unit = "lb"
    print(f"Your weight is: {round(weight, 1)} {unit} ")
elif unit == "L" or unit == "l":
    weight = weight / 2.2046
    unit = "kg"
    print(f"Your weight is: {round(weight, 1)} {unit} ")
else:
    print(f"{unit} was not valid!")



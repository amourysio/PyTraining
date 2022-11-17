# Logical operator = used on conditional statment

#           and = checks two or more conditional is True
#           or = checks if at least one condition is True
#           not = True if condition is False, vice versa

temp = 20
sunny = False
# if temp > 0 and temp < 30:
# if 0 < temp < 30:

if temp <= 0 or temp >= 30:
    print(f"The temperature is good! {temp}C")
else:
    print(f"The temperature is bad! {temp}C")

if sunny:
    print(f"{sunny} It is sunny outside!")
else:
    print(f"{sunny} It is cloudy outside!")
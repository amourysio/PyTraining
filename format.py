# format specifiers = {value:flags}

price1 = 3000.14159
price2 = -987.65
price3 = 12.34

print(f"Price1 is ${price1:+,.2f}")
print(f"Price2 is ${price2:,}")
print(f"Price3 is ${price3:.1f}")
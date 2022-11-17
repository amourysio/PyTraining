card_number = "374245455400126"
card_number = card_number.replace("-","")
card_number = card_number.replace(" ","")
card_number = card_number[::-1]

sum_odd_digits = 0
sum_even_digits = 0
for x in card_number[::2]:
    sum_odd_digits += int(x)

for x in card_number[1::2]:
    x = int(x) * 2
    if x >= 10:
        sum_even_digits += (1 +(x % 10))
    else:
        sum_even_digits += x

total = sum_odd_digits + sum_even_digits

if total % 10 == 0:
    print("Valid!")
else:
    print("Invalid!")
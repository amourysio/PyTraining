email = "Armoury123@gmail.com"
index = email.index("@")

# username = email[:index]
# domain = email[index + 1:]
username = email[:email.index("@")]
domain = email[email.index("@") + 1:]

print(f"Your username is {username} and domain is {domain}")

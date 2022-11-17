def hello():
    print("Hello")


print(hello)

say = hello
hello()
say()
print(say)

text = print
text("Get from Print")
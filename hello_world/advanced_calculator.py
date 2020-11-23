print("""sum:
multiply:
substract:
divide:
""")
word=input("Enter from here: ")
x=int(input("please enter first num: "))
y=int(input("please enter second number:"))

if word.lower() == "sum":
    print(x + y)
elif word.lower() == "multiply":
    print(x * y)
elif word.lower() == "substract":
    print(x - y)
elif word.lower() == "divide":
    print(x/y)
else:
    print("please enter a valid input")

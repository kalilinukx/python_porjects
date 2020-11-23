def Fizz_Buzz():
    num = int(input("plz enter a number:"))
    if num%3==0 and num%5==0:
        print("Fizz_Buzz")
    elif num%3==0:
        print("Fizz")
    elif num%5==0:
        print("Buzz")
    else:
        print(num)
Fizz_Buzz()

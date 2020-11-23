try:
    # this program is of the try and accept block
    age = int(input("age:"))
    income = 20000
    risk = income / age
    print(age)
except ValueError:
    print("invalid value")
except ZeroDivisionError:
    print("age can't be zero")

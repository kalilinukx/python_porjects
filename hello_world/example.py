x = int(input("Enter  any number : "))
s = 0
for i in range(x + 1):
    s += i
    # print(i)
    for j in range(i):
        s = s + j

print("sum is ", s)

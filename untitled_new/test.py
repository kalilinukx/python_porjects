# passing values to the function
# default arguments


def power(x, n=3):
    ans = 1
    for i in range(0,n):
        ans = ans*x
    return ans


print(int("10111111010001", 2))
output = []
n = 10
for i in range(n):
    if n%2 != 0:
        temp = n % 2
        n = n // 2
        output.append(temp)
# for item in output:
#     list
print(output[::-1])
for item in output:
    print(item,end="")

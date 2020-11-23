n1=0
n2=1

num=int(input("range please: "))
for i in range(num):
    if num==1:
        print(n1)
    else:


        print(f'{n1}',end=" ")
        sum = n1 + n2
        n1 = n2
        n2 = sum

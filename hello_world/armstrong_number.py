num=371
sum=0
# z = input("Enter the size of the digit : ")
temp=num
while temp>0:
    digit=temp%10
    sum+=digit**3
    temp//=10
# displaying the output of the programme

if num==sum:
    print(num, "is an armstrong number")
else:
    print(num,"this is not an armstrong number :")








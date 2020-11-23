list=[1,2,3,1,3,6,4,78,54,32]
output=[]
inititial=list[0]
for item in list:
    if item not in output:
        output.append(item)


print(output)
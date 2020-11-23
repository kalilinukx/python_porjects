#this is going to be 2 dimensional list

row =[
[1,2,3],
[3,4,5],
[23,45,67],
[12,35,78]
    ]
#for rows in row:
#print(row[1][0])
numbers=[5,2,1,7,4]
numbers.insert(0,10)
print(numbers)
numbers.remove(5)
numbers.pop()
print(numbers)
#print(numbers.index(5))
print(numbers.count(5))
numbers.sort()
print(numbers)
numbers2=numbers.copy()
numbers.append(23)
print(numbers)
print(numbers2)
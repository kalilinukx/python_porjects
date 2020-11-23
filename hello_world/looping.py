#while condition
i=1
while i<=5:
    print('$'*i)
    i+=1
    for x in range(4):
        for y in range(3):
            print(f'{x},{y}')



            number=[5,2,5,2,2]
            for x_count in number:
                output=""
                for count in range(x_count):
                    output+='x'
                print(output)


list=[5,2,5,2,2]
for roe in list:
    print('*'*roe)
for i in range(1,11):
    for j in range(1,11):
        print(f' table of {j} is',{j*i})
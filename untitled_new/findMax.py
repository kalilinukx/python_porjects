def findMaximum(list):
    max = list[0]
    for i in list:
        if i > max:
            max = i



    return max
print(findMaximum([1,2,4,7,21,3]))

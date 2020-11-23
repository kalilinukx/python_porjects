# cook your dish here
import re

numberOfCasesRaw = input()
numberOfCases = int(re.sub("\D","",numberOfCasesRaw))
digits = []
mainArr = []
counter = 0
s =[]

def convert(s):
    new = ""
    for x in s:
        new += x
    return new


while counter < numberOfCases:
    inputNumber = str(input())
    digits = [str(i) for i in str(inputNumber)]


#print(digits)


    s = digits.copy()
    size = len(digits)
    for i in range(0,size):
        digits.pop(i)
        mainArr.append(int(convert(digits)))
        digits.insert(i, s[i])

    print(min(mainArr))
    counter += 1
    mainArr= []
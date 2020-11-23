import random_number as rd
import copy
ls = []
for i in range(10):
    x = rd.randint(1,100)
    ls.append(x)

another_list = copy.deepcopy(ls)
# print(ls)
# print("\n")
#
# print(ls.index(ls[0]))


x = max(another_list)

another_list.remove(x)
y = max(another_list)

another_list.remove(y)
z = max(another_list)

another_list.remove(z)
print(another_list)
print(ls)


output = []
another_output = []
third_output = []


for item in ls:
    if item == x:
        break
    output.append(item)


# final_list = list(set(ls).difference(set(output)))
# print(final_list)

# for elements in final_list:
#     if elements == y:
#         break
#     another_output.append(elements)


for i in ls:
    if i == y:
        break
    another_output.append(i)

for j in ls:
    if j == z:
        break
    third_output.append(j)


print(output)
print(another_output)
print(third_output)
second_output = list(set(output).difference(set(another_output)))
print(second_output)
# for item in another_list:
#     if
# ls.sort()
# print(ls)

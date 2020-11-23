# nums = {1, 2, 3, 4, 5, 6}
# nums = {0, 1, 2, 3} & nums
# nums = filter(lambda x: x > 1, nums)
# print(len(list(nums)))
# import converters
# # # # converters.kg_to_lbs()
# use a stack data structure to convert integer  to binary
def int_to_bin(num):
    output = []
    while num!=0:
        if num%2 == 0:
            temp = num%2
            num = num//2
            output.append(temp)
    return output

print(int_to_bin(120))
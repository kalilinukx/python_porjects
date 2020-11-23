def find_max(numbers):
    maximum = numbers[0]
    for num in numbers:
        if num > maximum:
            maximum = num
    return print(maximum)


find_max([12, 23, 53, 72, 15])




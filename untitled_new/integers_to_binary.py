from new import Stack
def div_by_two(dec_num):
    s = Stack()
    while dec_num > 0:

        remainder = dec_num % 2
        s.push(remainder)
        dec_num = dec_num // 2

    bin_num = ""
    while not s.is_empty():
        bin_num += str(s.pop())

    return print(bin_num)
div_by_two(12)

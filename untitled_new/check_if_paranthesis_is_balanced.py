from new import Stack


def is_match(p1, p2):
    # if p1 == "(" and p2 == ")":
    #     return True
    # elif p1 == "{" and p2 == "}":
    #     return True
    # elif p1 == "[" and p2 == "]":
    if p1 + p2 in ["{}","[]","()"]:
        return True
    else:
        return False


def if_paren_balanced(paren_string):
    s = Stack()
    is_balanced = True
    index = 0
    count = 0
    trump = 0

    while index < len(paren_string) and is_balanced:
        paren = paren_string[index]
        # print(s.get_stack())
        # print()
        # print(paren_string)
        if paren in "([{":
            count += 1
            s.push(paren)
        else:
            trump +=1
            if s.is_empty():
                is_balanced = False
            else:
                top = s.pop()
                if not is_match(top, paren):
                    is_balanced = False
        index += 1
    if len(paren_string) %2 == 0 and count  == trump:
        if s.is_empty and is_balanced:
            return "Balanced"
    else:
        return "Not Balanced"


print(if_paren_balanced("{[[]]}"))

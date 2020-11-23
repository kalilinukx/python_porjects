

class Stack():
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def is_empty(self):
        return self.items == []

    def get_stack(self):
        return self.items

    def peek(self):
        if self.is_empty() != []:
            return self.items[-1]

    def multiply(self):
        if self.is_empty() != []:
            return self.items * 2

    def remove_everything(self):
        for i in range(3):
            if self.items != []:
                del self.items[0]
        return self.items == []
        # return self.is_empty()
#
#
# s = Stack()
#
# s.push("A")
# s.push("B")
# s.push("H")
#
# print(s.get_stack())
#
# s.remove_everything()
# # s.pop()
# # s.pop()
# # s.pop()
# # print()
# # s.push(3)
# print(s.is_empty())
# # print(s.peek())
# # print(s.get_stack())
# # print(s.multiply())
# print(s.remove_everything())
#
# # print(len())
# print(s.items)
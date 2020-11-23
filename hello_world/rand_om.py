import random_number
# python enhancement proposal


class Dice:
    def roll (self):
        first = random_number.randint(1, 6)
        second = random_number.randint(1, 6)
        return (first,second)

dice=Dice()
print(dice.roll())
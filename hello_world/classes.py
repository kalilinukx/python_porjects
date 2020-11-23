def say_hi():
    print("i am mise")


class Person:
    def __init__(self, name):
        self.name = name
        
    def talk(self):
        print(f'i am {self.name}')

    def say_hi(self):
        print("i am mise")


person1 = Person(" john smith")
bob = Person("bob smith")
bob.talk()
person1.talk()
person1.say_hi()
print(person1.name)

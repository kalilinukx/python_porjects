import string
import random_number


def generete_password(size):
    all_chars = string.ascii_letters + string.digits + string.punctuation
    password = ""
    for char in range(size):
        rand_char = random_number.choice(all_chars)
        password = password + rand_char
    return password


history = ''
for i in range(2):
    pass_len = int(input("How many characters in your name ?"))
    new_password = generete_password(pass_len)
    history += history + new_password + "\n"
    print("Your new password", new_password)

print(f'Your history of passwords are  {history}')

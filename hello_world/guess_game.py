secret_number=9
guess_limit=3
guess_count=0
while guess_count<guess_limit:
    guess=int(input(" enter your guess: "))
    guess_count+= 1
    if guess==secret_number:
        print("you guessed it really right ")
        break
else:
    print("you didn't guess that it in right no of chances")


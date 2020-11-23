import random_number
secret_number=str(random_number.randint(10, 99))
print("Guess the numbern.it contains 2 digits.")
remaining_try=7
while remaining_try>0:
    player_guess=input("Enter your guess:")

    if player_guess==secret_number:
        print('Yay, you guessed it !')
        print('YOU WIN.')

    else:
        bulls=0
        cows=0
        if player_guess[0]==secret_number[0]:
            bulls+=1
        if player_guess[1]==secret_number[1]:
            bulls+=1
        if player_guess[0]==secret_number[1]:
            cows+=1
        if player_guess[1]==secret_number[1]:
            cows+=1

        print('Bulls:',bulls)
        print('cows',cows)
        remaining_try-=1
        if remaining_try<1:
            print('You lost the game.')
            break
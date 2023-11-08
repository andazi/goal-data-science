import random

trials = 3

while trials > 0:
    # generating random number between 1 and 20
    rand_number = random.randint(1,20)
    print(rand_number)
    # giving player 3 trials
    for i in range(trials):
        # input by default is a string
        guess = int(input('Guess a number between from 1 to 20?      '))
        if guess == rand_number:
            break
        else:
            if guess > rand_number:
                print('Number is too high')
            else:
                print('Number is too low')
        trials -= 1
    if i < trials:
        print('GAMEOVER, YOU LOSE')            
    trials = 0

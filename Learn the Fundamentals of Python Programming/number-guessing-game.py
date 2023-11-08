import random

trials = 3
# generating random number between 1 and 20
rand_number = random.randint(1,20)    
list_of_guesses = []
#print(rand_number)
while trials > 0:    

    guess = int(input('Guess a number between from 1 to 20?      '))

    list_of_guesses.append(guess)
    if guess == rand_number:
        print('You have guessed correctly')
        print('You WON')
        # end while loop
        trials = 0
    else:
        if guess > rand_number:
            print('Number is too high')
        else:
            print('Number is too low')
  
    trials -= 1
    if trials == 0:
        print('GameOver, you LOSE')
        
print ("You guessed the following numbers: ", list_of_guesses)

# we used the random module and called randint
# randint method generates random interger
# rand_number outside the while loop to avoid the rand_number from running again
# while loop to track the number of times player would play
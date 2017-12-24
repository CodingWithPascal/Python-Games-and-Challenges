import random
number = random.randint(0,100)

Win = True
user = int(input('Guess a number between 0 and 100: '))
guess_number = 0
while Win is True:
    guess_number +=1
    if user == number:
        print('You win! It took ' + str(guess_number) + ' guesses.')
        Win = False
        exit()
    elif user < number:
        user = int(input('Too low! Guess again: '))
    elif user>number:
        user = int(input('Too high! Guess again: '))


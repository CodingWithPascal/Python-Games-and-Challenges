import random

objects = ['Rock', 'Paper', 'Scissors']

Win_condition = {'Rock': 'Scissors',
                 'Scissors': 'Paper',
                 'Paper': 'Rock'}

Play_Again = True
while Play_Again is True:
    try:
        answer = input('Rock, Paper, Scissors, Shoot!: ')
    except KeyError:
        print('enter an item weirdo: ')
        answer = input('Rock, Paper, Scissors, Shoot!: ')

    print('Your answer is: ' + answer)
    comp_input = objects[random.randint(0, 2)]
    print('Computer choice: ' + comp_input)

    if answer == comp_input:
        print('Tie!')
        response = input('Do you want to play again?: ')
        if response == 'Yes':
            Play_Again = True
        if response != 'Yes':
            break
    elif Win_condition[answer] == comp_input:
        print('You win, rockstar!')
        response = input('Do you want to play again?: ')
        if response == 'Yes':
            Play_Again = True
        if response != 'Yes':
            break

    else:
        print('You lose, dumbass!')
        response = input('Do you want to play again?: ')
        if response == 'Yes':
            Play_Again = True
        if response != 'Yes':
            break

print('Thanks for playing!')

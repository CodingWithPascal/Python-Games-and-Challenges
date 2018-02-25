import random

print("Let's play rock, paper, scissors!")
answer = input('Rock, Paper, Scissors, Shoot!: ')
print('Your answer is: ' + answer)

objects = ['Rock', 'Paper', 'Scissors']
comp_input = objects[random.randint(0,2)]
print('Computer choice: ' + comp_input)

if answer == comp_input:
    print('Tie!')
elif answer == 'Rock' and comp_input == 'Paper':
    print('You lose, loser!')
elif answer == 'Rock' and comp_input == 'Scissors':
    print('You win, rockstar!')
elif answer == 'Paper' and comp_input == 'Scissors':
    print('You lose, loser!')
elif answer == 'Paper' and comp_input == 'Rock':
    print('You win, rockstar!')
elif answer == 'Scissors' and comp_input == 'Rock':
    print('You lose, loser!')
elif answer == 'Scissors' and comp_input == 'Paper':
    print('You win, rockstar!')

response = input('Do you want to play again? (Yes/No): ')
if response == 'No':
    print('Thanks for playing!')
elif response == 'Yes':
    print("Shijit's gonna teach this")
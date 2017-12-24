import random

print(random.randint(0,1))

coin = ['heads', 'tails']


cointoss = coin[random.randint(0,1)]
print(cointoss)
answer = input('Want to play again? (Type "Y"/"N")')

while answer == 'Y' :
    print(coin[random.randint(0,1)])
    answer = input('Want to play again? (Y/N)')
else:
    print('Thanks for playing!')
 



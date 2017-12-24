import random

print(random.randint(1,20))

answer = input('Roll again? (Type Y/N): ')
while answer == 'Y':
    print(random.randint(1, 20))
    answer = input('Roll again? (Type Y/N): ')
else:
    print('Thanks for playing!')
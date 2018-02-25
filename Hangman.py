h = ['head', 'body', 'left leg', 'right leg', 'left arm', 'right arm']
word = 'candy'
word_length = len(word)
dashes = ''
for i in word:
    dashes += '- '
print(dashes)
u = input('Letter? ').lower()
while




if u.lower() in word:
    print('True')
else:
    print('You guessed wrong!')
    print(h[0])

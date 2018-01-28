sentence1 = 'I went to the store and bought some cheese today.'
sentence2 = 'I went to the store and bought some cheese hoorah.'
sentence3 = 'Shijit says he owns a store'
sentence4 = 'Luke is taller than Shijit'


def translate(sent, english, croatian):
    new_sentence = ''
    for item in sent.split(' '):
        if item == english:
            new_sentence = new_sentence + croatian + ' '
        else:
            new_sentence = new_sentence + item + ' '
    return new_sentence

print(translate(sentence1, 'cheese', 'sir'))
print(translate(sentence2, 'some', 'malo'))
print(translate(sentence3, 'says', 'kaže da') )
print(translate(sentence4, 'taller', 'viši'))

        # shijit's hint: make a "new sentence" and throw words into new sentence by adding them and then wen you it the word
# to translate, just throw in the translated word instead.
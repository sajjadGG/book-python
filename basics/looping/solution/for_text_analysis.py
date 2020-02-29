TEXT = """
    We choose to go to the Moon.
    We choose to go to the Moon in this decade and do the other things.
    Not because they are easy, but because they are hard.
    Because that goal will serve to organize and measure the best of our energies and skills.
    Because that challenge is one that we are willing to accept.
    One we are unwilling to postpone.
    And one we intend to win
"""

total_sentences = 0
total_words = 0
total_chars = 0
total_letters = 0
total_commas = 0
total_adverbs = 0


for sentence in TEXT.split('.'):

    sentence = sentence.strip()
    words = sentence.split()
    characters = sentence.replace(',', '')
    letters = characters.replace(' ', '')

    total_sentences += 1
    total_words += len(words)
    total_chars += len(characters)
    total_letters += len(letters)
    total_commas += sentence.count(',')

    for word in words:
        if word.endswith('ly'):
            total_adverbs += 1


print(f'Sentences: {total_sentences}')
print(f'Words: {total_words}')
print(f'Characters: {total_chars}')
print(f'Letters: {total_letters}')
print(f'Commas: {total_commas}')
print(f'Adverbs: {total_adverbs}')



# Alternative Solution
print('-' * 50)
TEXT = 'We choose to go to the Moon. We choose to go to the Moon in this decade and do the other things. Not because they are easy, but because they are hard. Because that goal will serve to organize and measure the best of our energies and skills. Because that challenge is one that we are willing to accept. One we are unwilling to postpone. And one we intend to win'
text = TEXT.strip()

output = {
    'Sentences': len(text.split('.')),
    'Words': len(text.split(' ')),
    'Characters': len(text.replace('. ', '')),
    'Letters': len(text.replace('.', '').replace(' ', '').replace(',', '')),
    'Commas': text.count(','),
    'Adverbs': text.count('ly'),
}

for key, value in output.items():
    print(f'{key}: {value}')





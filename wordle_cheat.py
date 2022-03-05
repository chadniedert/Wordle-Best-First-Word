# Creates all_five_letter_words list from five_letter_words.txt
# five_letter_words.txt was created in best_first_word.ipynb
with open('five_letter_words.txt') as f:
    lines = f.readlines()

all_five_letter_words = []

for word in lines:
    all_five_letter_words.append(word.strip('\n').upper())

round = 1
feedback = []
last_wordle = []

print('DIRECTIONS')
print('Step 1 --> Provide the Wordle word you played when prompted for \'Played word >>> \'')
print('Step 2 --> Use a \'G\' to indicate a letter from the most recently played Wordle word that is in the word and in the correct position.')
print('           Use a \'Y\' to indicate a letter from the most recently played Wordle word that is in the word but NOT in the correct position.')
print('           Use a \'-\' to indicate a letter from the most recently played Wordle word that is in the word but NOT in the correct position.')
print()
print('EXAMPLE')
print('If the Wordle word is \'THINK\', and the user plays \'FAINT\' then the user would type \'--GGY\' when prompted for \'Wordle Feedback >>> \'.')
while (round <= 6 and feedback !=  ['G', 'G', 'G', 'G', 'G']):
    wd = input('Played word >>> ')
    fb = input('Wordle Feedback >>> ')
    feedback = []
    last_wordle = []   
    for i in wd:
        last_wordle.append(i)
    for i in fb:
        feedback.append(i)
    
    round += 1



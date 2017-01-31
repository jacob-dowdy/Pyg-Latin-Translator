# Pig Latin Translator
# variable made for the end of the word
pyg = 'ay'
# grabs user input
original = raw_input('Enter a word:')
# verifies that there are characters entered and that they are lowercase
if len(original) > 0 and original.isalpha():
# makes the word lower case, stores the first letter of the word, and combines all of the variables for the final translation 
    word = original.lower()
    first = word[0]
    new_word = word + first + pyg
    new_word = new_word[1:]
    print new_word
else:
    print 'empty'

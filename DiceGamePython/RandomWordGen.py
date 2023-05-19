#  choose a random word to be used as the word to guess
#  display the word to the user as hyphens ( hat would be _ _ _) 
#  ask the user to guess a letter that may be in the word
#  if the user's guess is wrong then display a section of the hanged man
#  if the user's guess is right then display the word as hyphens with the correct letter that was guessed in place of a hyphen and ask to guess again

# build a function to choose a random word from a list of words

# build a function to display the word as hyphens (the length of the word = how many hyphens)

# build a function to ask the user for a guess

# build a function to check if the user's guess exists in the word

# build a function to display the current state of the hanged man

#  ___ 
#  |  | 
#  0  | 
# /|\ |
# / \ |
#_____|_____

# build a function to choose a random word from a list of words

RandWords = ["Scary", "Angel","Videos","Inbox","pneumonoultramicroscopicsilicovolcanoconiosis","Google","Tuesday","Console","Shell","Luna","CodeColab"]

import random

def funcWords():
    for i in range(): 
        i = len(RandWords)
user_input = input("Guess an index: ")
numGen = random.randint(0, RandWords)
hidden_word = "-" * len(numGen[user_input])
print(f"This is the hidden word" + {RandWords[user_input]}) 

hidden_word = hidden_word[:RandWords] + user_input + hidden_word[RandWords + 1:]

print(hidden_word)

print(RandWords[user_input])

# build a function to display the word as hyphens (the length of the word = how many hyphens)
#def hangMan(RandWords, user_input):


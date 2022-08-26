'''
This program generates a random word and gives you six tries to guess the word
'''
import time

#use pip install random-word to get this module
from random_word import RandomWords

r = RandomWords()

guess = []

#Gets the random word with these paramaters
answer = r.get_random_word(minLength=5, maxLength=5, minCorpusCount=6000, excludePartOfSpeech="adjective,adverb")

#This condition is because sometimes the random word would have a value of NONE
while type(answer) == ' NoneType':
  answer = r.get_random_word(minLength=5, maxLength=5, minCorpusCount=6000, excludePartOfSpeech="adjective,adverb")

tries = 6


def instructions():
  print('Guess the word in at least six tries.')
  time.sleep(1)
  print('Each word must be a valid five letter word.\nHit enter to submit your word.')
  time.sleep(1)
  print('Good luck!')

instructions()
 

for x in range(6):
  u = 0
  guess = input('\nInput your five letter guess here\n')

  guessLength = len(guess)
  print(guessLength)

  if guess == answer:
     print('you have guessed the word')
     break

  if guessLength > 5:
      print('Guess too long, try again')

#Checks the guess and compares it to the answer
  for g in range(5):
    if answer[g] == guess[u] and guessLength <= 5:
      print(f'{guess[u]} is correct')
      u += 1
    elif guess[u] in answer and guessLength <= 5:
      print(f'{guess[u]} is in the wrong place but in the word')
      u += 1
    else:
      print(f'{guess[u]} is not in the word at all')
      u += 1
  
  if guessLength <= 5:
    tries -= 1
    print(f'\nYou have {tries} tries left.')


if tries == 0:
    print(f'\n\nThe word was {answer}')
    print('\nGood try, hope you play again')
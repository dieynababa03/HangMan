import random

stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']
# Generate random word from list
wordList = ["muschi", "software", "engineer", "backend", "activate", "narrow", "garage","exhibition", "dentist", "sausage", "factory", "performance", "classroom", "orangutan", "consciousness", "explosion", "luffy", "kittens", "decoration", "mutation", "office", "arrow", "marvel", "blackbeard"]
wordToGuess = random.choice(wordList)
wordToGuess = list(wordToGuess)
length = len(wordToGuess)
lives = 6
gameCondition = False
display = []
for displayContents in range(length):
  display.append("_")
while not gameCondition and not lives == 0:
  for displayContents in display:
   print(displayContents, end=" ")
  print("\n")
  guess = input("Guess a letter: ")
  # Iterate through each of the characters
  # in wordToGuess
  for index in range(length):
    character = wordToGuess[index]
    # Check for a match
    if guess == character:
      display[index] = guess
  # Decrement lives if guess is wrong
  if guess not in wordToGuess:
    lives -= 1
    # Checking if user has run out of lives
    if lives == 0:
      print("You lose!")
  if "_" not in display:
    print("You Win!")
    gameCondition = True
  # Print hangman based on lives
  print(stages[lives])



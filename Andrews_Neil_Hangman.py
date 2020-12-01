'''
Hangman by Neil Andrews
Nov 2020
'''
from random import randint

# Import the list of words from the text document
textFile = open("word_list.txt","r")
content = textFile.read()
content = content.splitlines()

# Randomly select a word from the imported list
position = randint(0,len(content))
chosenWord = str(content[position])

wrongGuesses = 0
wrongLetters = []

# Generate a blank string of the chosen word
a = len(chosenWord)
guessedWord = ('*' * a)

# Convert the word into a string
listWord = list(guessedWord)

# Generate a list of gallows drawings
gallows = ["""
    ------|
    |/
    |
    |
    |\\
--------------
           """,
           """
    ------|
    |/    o
    |
    |
    |\\
--------------
           """,
           """
    ------|
    |/    o
    |     |
    |
    |\\
---------------
           """,
           """
    ------|
    |/    o
    |     |\\
    |
    |\\
---------------
           """,
           """
    ------|
    |/    o
    |    /|\\
    |
    |\\
---------------
           """,
           """
    ------|
    |/    o
    |    /|\\
    |     |
    |\\
---------------
           """,
           """
    ------|
    |/    o
    |    /|\\
    |     |
    |\\     \\
---------------
           """,
           """
    ------|
    |/    o
    |    /|\\
    |     |
    |\\   / \\
---------------
   HANG MAN!
            """]
# Clear the display screen
print('\n'*80)
print(f"\nYour word has {a} letters and you are allowed 7 incorrect guesses:")

# Inputting player's guess
def playerGuess():
    guess = input('\nPlease enter your next guess: \n')
    guess = guess.lower()
    return guess

# Main game loop
while True:
    print(gallows[wrongGuesses])
    print("Incorrect Letters:", wrongLetters, '\n')
    print(guessedWord)

    # Guess evaluation loop
    guess = playerGuess()
    print('\n'*80)

    # Test to see if player's guess is in chosenWord
    for num in range(0, a):
        if chosenWord[num] == guess:
            listWord[num] = guess
            guessedWord = ''.join(listWord)

    # If you have guessed all the letters in chosenWord you win
    if guessedWord == chosenWord:
        print("congratulations you win\n")
        break

    # Add an incorrect letter 'wrongLetters' string
    if guess not in chosenWord:
        wrongGuesses += 1
        wrongLetters.append(guess)

    # If you run out of guesses you lose
    if wrongGuesses == 7:
        print(gallows[wrongGuesses])
        print("you lose\n")
        print(f"the word was {chosenWord}\n")
        break

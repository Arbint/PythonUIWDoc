import requests
import random
from gameRunner import RunGame

def GetWords():
    url = "https://raw.githubusercontent.com/david47k/top-english-wordlists/master/top_english_words_lower_10000.txt"
    wordsResponse = requests.get(url)
    return wordsResponse.text.split()


def GetRandomWord(words):
    return random.choice(words)

def DisplayWord(word, guessedLetters):
    output = ""
    for letter in word:
        if letter in guessedLetters:
            output += letter
        else:
            output += "_"
       
    return output

def GetGuess(guessedAlready)->str:
    while True:
        guess = input("please take a guess\n>>>")
        if guess in guessedAlready:
            print(f"you have already guessed the letter: {guess}")
            continue

        if len(guess) != 1:
            print("please guess one letter at a time")
            continue

        if not guess.isalpha():
            print("invalid input, please type in a letter")
            continue

        return guess

def AllGuessed(guessedLetters, wordToGuess):
    for letter in wordToGuess: 
        if letter not in guessedLetters:
            return False

    return True 

@RunGame
def Hangman(testMode = False):
    wordToGuess = GetRandomWord(GetWords())
    guessedLetters = set()
    attempsLeft = 6

    print("Welcom to hangman")

    while attempsLeft > 0:
        if testMode:
            print(f"The word is: {wordToGuess}")

        print("\nword:", DisplayWord(wordToGuess, guessedLetters))
        print(f"Attempts left: {attempsLeft}")
        print(f"Guessed letters: {",".join(sorted(guessedLetters))}")

        guess = GetGuess(guessedLetters)
        if guess in wordToGuess:
            guessedLetters.add(guess)
        else:
            attempsLeft -= 1

        if AllGuessed(guessedLetters, wordToGuess):
            print(f"You Guessed It! The word is: {wordToGuess}")
            return

    print(f"You lose! the word is {wordToGuess}")


if __name__ == "__main__":
    Hangman(True)
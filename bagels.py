"""Bagels, a deductive logic game where you must guess a number based on clues."""

import random

NUM_DIGITS = 3
MAX_GUESSES = 10

def main():
    print("""Bagels - A deductive logic game.

I am thinking of a {} digit number with no repeated digits. Try to guess what it is. Here are some clueas:

when I say                it means
Pico                      one digit is correct, but in the wrong position
Fermi                     one digit is correct and in the right position
Bagels                    no digit is correct

""".format(NUM_DIGITS))

    while True:         # Main game loop
        # This stores the secret number the player needs to guess.
        secretNum = getSecretNum()
        print("I have thought up a number.")
        print("You have {} guesses to get it.".format(MAX_GUESSES))

        numGuesses = 1
        while numGuesses <= MAX_GUESSES:
            guess = ''
            # Keep looping until they enter a valid guess
            while len(guess) != NUM_DIGITS or not guess.isdecimal():
                print("Guess #{}: ".format(numGuesses))
                guess = input("> ")

            clues = getClues(guess, secretNum)
            print(clues)
            numGuesses += 1

            if guess == secretNum:
                break           # They're correct, so break out of this loop
            if numGuesses > MAX_GUESSES:
                print("You ran out of guesses.")
                print("The answer was {}.".format(secretNum))

        # ask player if they want to play again.
        print("Do you want to play again? (yes or no)")
        if not input("> ").lower().startswith('y'):
            break
    print("Thanks for playing!")


def getSecretNum():
    """Returns a string made up of NUM_DIGITS unique random digits."""
    numbers = list('0123456789')    # Create a list of digits 0 - 9
    random.shuffle(numbers)     # Shuffle the numbers list into random orderr

    # Get the first NUM_DIGITS digits in the list for the secret number.
    secretNum = ''
    for i in range(NUM_DIGITS):
        secretNum += str(numbers[i])
    return secretNum


def getClues(guess, secretNum):
    """Returns a string with pico, fermi, bagels clues for a guess and secret number pair."""
    if guess == secretNum:
        return "You got it!"

    clues = []

    for i in range(len(guess)):
        if guess[i] == secretNum[i]:
            clues.append("Fermi")
        elif guess[i] in secretNum:
            clues.append("Pico")
    if len(clues) == 0:
        return "Bagels"
    else:
        clues.sort()
        return ' '.join(clues)


if __name__ == '__main__':
    main()

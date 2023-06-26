# Write a txt file which has a word in each line like:
# Hands
# Legs
# India
# Crow
# Rain
# ...

# Write a python code to read the file and store the words in the list

# Write a function to guess a word randomly from the list.

# Now, write a function which asks user to guess the chosen word letter by letter.
# Show "incorrect" message to the wrong guessed letter. 
# Display  letters in the clue word that were guessed correctly. 

# Let say word is EVAPORATE

# >>> Welcome to Hangman!
# _ _ _ _ _ _ _ _ _
# >>> Guess your letter: S
# Incorrect!
# You left with 5 chances to guess.

# >>> Guess your letter: E
# E _ _ _ _ _ _ _ E
# ...
# And so on.


# 1)Only let the user guess 6 times, and tell the user how many guesses they have left.
# Keep track of the letters the user guessed.
# 2) If the user guesses a letter they already guessed, don’t penalize them - let them guess again.
# 3)When the player wins or loses, let them start a new game.

import random

def play_hangman_game():
    print("Time to play hangman game!")


    word = random.choice(open("words.txt", "r").read().split())
    guesses = ''
    turns = 6

    while turns > 0:
        failed = 0
        for char in word.upper():
            if char in guesses:
                print(char, end="")
            else:
                print("_", end="")
                failed += 1
        if failed == 0:
            print("\nYou won!")
            break

        guess = input("\nGuess a character: ").upper()

        if guess in guesses:
            print("You have already guessed that letter. Try again.")
            continue

        guesses += guess

        if guess not in word:
            turns -= 1
            print("Wrong")
            print("You have", turns, "more guesses.")
            if turns == 0:
                print("You Lose. The word was:", word)

# Main game loop
def play_game():
    while True:
        play_hangman_game()
        play_again = input("Do you want to play again? (yes/no): ").lower()
        if play_again != "yes":
            print("Thank you for playing Hangman!")
            break

play_game()

# Guess-the-Word-
This project implements a word guessing game in Python, following a four-part assignment. The game challenges the player to guess a secret word one letter at a time while enforcing input validation and tracking incorrect guesses.

Assignment Breakdown
Part 1 – Secret Word and User Input

Secret Word Variable:
A variable stores the secret word.
Retrieving User’s Guess:
The get_guess() function repeatedly prompts the user for input until a single, lowercase letter is entered. Input validation ensures the guess is exactly one character and in lowercase.
Part 2 – Displaying Progress with Dashes

Dashes Variable:
A string of dashes is created, with its length equal to that of the secret word, to represent unguessed letters.
Updating the Display:
The update_dashes() function takes the secret word, the current state of the dashes, and the latest guess to reveal correctly guessed letters without erasing previous correct guesses.
Part 3 – Win/Lose Logic

Game Loop:
The game runs in a loop that continues until the user either guesses the entire word or runs out of incorrect guesses.
Tracking Incorrect Guesses:
A variable guesses_left starts at 10 and decrements for each incorrect guess.
End-of-Game Message:
After the loop, the program prints whether the player has won (by guessing the word) or lost (by exhausting the allowed incorrect guesses).
Part 4 – Random Word Selection

Word List:
A list of words is provided.
Random Choice:
The secret word is randomly chosen from the list using random.choice(), ensuring variety in each playthrough.

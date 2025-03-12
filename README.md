# Guess the Word Game

This project is a Python-based word guessing game where the player tries to reveal a secret word by guessing one letter at a time. The game provides feedback on correct and incorrect guesses and tracks the number of incorrect attempts allowed.

## Features

- **Random Word Selection**
  - A secret word is randomly selected from a predefined list.

- **Input Validation**
  - Ensures that the user's guess is exactly one character.
  - Confirms that the guess is a lowercase letter.

- **Progress Display**
  - Displays the secret word as a series of dashes.
  - Correctly guessed letters replace the corresponding dashes.

- **Win/Lose Logic**
  - The game allows a maximum of 10 incorrect guesses.
  - Displays a win message if the player reveals the whole word.
  - Displays a lose message if the player runs out of guesses.

## Code Overview

- **Secret Word and Dashes**
  - The secret word is selected randomly.
  - A string of dashes, matching the length of the secret word, is created to represent unguessed letters.

- **`get_guess` Function**
  - Continuously prompts the user until a valid guess (one lowercase letter) is entered.

- **`update_dashes` Function**
  - Updates the displayed dashes by revealing letters that match the user's guess.

- **Game Loop**
  - Continues until the word is fully guessed or the user runs out of guesses.
  - Tracks the number of incorrect guesses and provides feedback.

- **End-of-Game Message**
  - Informs the player if they have won or lost, displaying the secret word.



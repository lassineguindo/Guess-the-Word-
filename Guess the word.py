import random

words = ["bowie", "state", "university", "computer", "technology"]
secret_word = random.choice(words)
dashes = "-" * len(secret_word)
guesses_left = 10

def get_guess():
    while True:
        guess = input("Guess: ")
        if len(guess) != 1:
            print("Your guess must have exactly one character!")
        elif not guess.islower():
            print("Your guess must be a lowercase letter!")
        else:
            return guess

def update_dashes(secret, current_dashes, guess):
    result = ""
    for i in range(len(secret)):
        if secret[i] == guess:
            result += guess
        else:
            result += current_dashes[i]
    return result

while dashes != secret_word and guesses_left > 0:
    print(dashes)
    print(f"{guesses_left} incorrect guesses left.")
    guess = get_guess()
    if guess in secret_word:
        print("That letter is in the word!")
        dashes = update_dashes(secret_word, dashes, guess)
    else:
        print("That letter is not in the word!")
        guesses_left -= 1

if dashes == secret_word:
    print(f"Congrats! You win. The word was: {secret_word}")
else:
    print(f"You lose. The word was: {secret_word}")



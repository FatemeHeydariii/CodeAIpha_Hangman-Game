import random

words = ["python", "computer", "coding", "program", "linux"]

word = random.choice(words)
display = ["_"] * len(word)

attempts = 6
guessed_letters = []

hangman = [
    """
     +---+
     |   |
         |
         |
         |
         |
    =========
    """,

    """
     +---+
     |   |
     O   |
         |
         |
         |
    =========
    """,

    """
     +---+
     |   |
     O   |
     |   |
         |
         |
    =========
    """,

    """
     +---+
     |   |
     O   |
    /|   |
         |
         |
    =========
    """,

    """
     +---+
     |   |
     O   |
    /|\\  |
         |
         |
    =========
    """,

    """
     +---+
     |   |
     O   |
    /|\\  |
    /    |
         |
    =========
    """,

    """
     +---+
     |   |
     O   |
    /|\\  |
    / \\  |
         |
    =========
    """
]

print("Welcome to Hangman!")
print(" ".join(display))

while attempts > 0 and "_" in display:

    guess = input("Guess a letter: ").lower()

    if len(guess) != 1 or not guess.isalpha():
        print("Please enter one letter.")
        continue

    if guess in guessed_letters:
        print("You already guessed this letter!")
        continue

    guessed_letters.append(guess)

    if guess in word:

        print("Correct!")

        for i in range(len(word)):
            if word[i] == guess:
                display[i] = guess

    else:

        attempts -= 1

        print("Wrong!")
        print("Attempts left:", attempts)

        # تعداد اشتباه‌ها = 6 - attempts
        wrong_guesses = 6 - attempts

        print(hangman[wrong_guesses])

    print(" ".join(display))
    print()


if "_" not in display:

    print("******* You won! ********")
    print("The word was:", word)

else:

    print(hangman[6])
    print("Game over!")
    print("The word was:", word)
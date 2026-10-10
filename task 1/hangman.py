import random

# List of predefined words
words = ["python", "computer", "program", "developer", "coding"]

# Select a random word
word = random.choice(words)

# Store guessed letters
guessed_letters = []

# Number of incorrect guesses
wrong_guesses = 0
max_wrong_guesses = 6

print("================================")
print("       WELCOME TO HANGMAN")
print("================================")
print("Guess the word one letter at a time!")
print("You have 6 wrong guesses.\n")

# Main game loop
while wrong_guesses < max_wrong_guesses:

    # Display the word
    display_word = ""

    for letter in word:
        if letter in guessed_letters:
            display_word += letter + " "
        else:
            display_word += "_ "

    print("Word:", display_word)

    # Check if the word is completely guessed
    if all(letter in guessed_letters for letter in word):
        print("\n🎉 Congratulations! You guessed the word!")
        print("The word was:", word)
        break

    # Get user's guess
    guess = input("\nEnter a letter: ").lower()

    # Validate input
    if len(guess) != 1 or not guess.isalpha():
        print("Please enter only one letter.")
        continue

    # Check if letter was already guessed
    if guess in guessed_letters:
        print("You already guessed that letter.")
        continue

    # Add letter to guessed list
    guessed_letters.append(guess)

    # Check the guess
    if guess in word:
        print("✅ Correct guess!")
    else:
        wrong_guesses += 1
        print("❌ Wrong guess!")
        print("Wrong guesses:", wrong_guesses, "/", max_wrong_guesses)

else:
    print("\n💀 Game Over!")
    print("The correct word was:", word)
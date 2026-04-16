import random

# Step 1: word list
words = ["apple", "tiger", "chair", "plant", "bread"]

# Step 2: choose random word
word = random.choice(words)

# Step 3: display blanks
guessed_word = ["_"] * len(word)

# Step 4: variables
guessed_letters = []
wrong_guesses = 0
max_wrong = 6

print("Welcome to Hangman!")

# Step 5: game loop
while wrong_guesses < max_wrong and "_" in guessed_word:
    print("\nWord:", " ".join(guessed_word))
    print("Wrong guesses left:", max_wrong - wrong_guesses)
    print("Guessed letters:", ", ".join(guessed_letters))

    guess = input("Guess a letter or the full word: ").lower()

    if not guess.isalpha():
        print("Please enter only letters!")
        continue

    # Full word guess
    if len(guess) > 1:
        if guess == word:
            guessed_word = list(word)
            break
        else:
            print("Wrong guess!")
            wrong_guesses += 1
            continue

    # Single letter guess
    if guess in guessed_letters:
        print("You already guessed that letter!")
        continue

    guessed_letters.append(guess)

    if guess in word:
        print("Correct guess!")
        for i in range(len(word)):
            if word[i] == guess:
                guessed_word[i] = guess
    else:
        print("Wrong guess!")
        wrong_guesses += 1

# Step 6: result
if "_" not in guessed_word:
    print("\nYou won! The word was:", word)
else:
    print("\nYou lost! The word was:", word)
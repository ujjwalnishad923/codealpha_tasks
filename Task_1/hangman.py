import random

# 1. List of words
words = ["python", "coding", "computer", "program", "developer"]

# 2. Choose a random word
word = random.choice(words)

# 3. Hide the word
hidden_word = ["_"] * len(word)

# 4. Maximum wrong guesses
guesses = 6

print("Welcome to the Hangman Game!")
print("Guess the word one letter at a time.")

# 5. Game loop
while guesses > 0 and "_" in hidden_word:

    print("\nWord:", " ".join(hidden_word))
    print("Remaining guesses:", guesses)

    # 6. Get a letter from the user
    char = input("Enter a letter: ").lower()

    # 7. Check the letter
    if char in word:

        # 8. Reveal the correct letter
        for i in range(len(word)):
            if word[i] == char:
                hidden_word[i] = char

        print("Correct guess!")

    else:
        guesses -= 1
        print("Wrong guess!")

# 9. Final result
if "_" not in hidden_word:
    print("\nCongratulations! You won!")
    print("The word was:", word)
else:
    print("\nGame Over!")
    print("The word was:", word)
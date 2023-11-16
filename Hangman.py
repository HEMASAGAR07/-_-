import random


word_list = ["apple", "banana", "cherry", "date", "elderberry", "fig", "grape"]

def choose_word():
    return random.choice(word_list)

def display_word(word, guessed_letters):
    displayed_word = ""
    for letter in word:
        if letter in guessed_letters:
            displayed_word += letter
        else:
            displayed_word += "_"
    return displayed_word

def hangman():
    word_to_guess = choose_word()
    guessed_letters = []
    attempts = 6

    print("Welcome to Hangman!")
    print(display_word(word_to_guess, guessed_letters))

    while True:
        guess = input("Guess a letter: ").lower()

        if guess in guessed_letters:
            print("You've already guessed that letter. Try again.")
            continue

        guessed_letters.append(guess)

        if guess in word_to_guess:
            print("Good guess!")
        else:
            print("Incorrect guess!")
            attempts -= 1

        displayed = display_word(word_to_guess, guessed_letters)
        print(displayed)

        if displayed == word_to_guess:
            print("Congratulations, you've won! The word was:", word_to_guess)
            break

        if attempts == 0:
            print("You've run out of attempts. The word was:", word_to_guess)
            break

if __name__ == "__main__":
    hangman()

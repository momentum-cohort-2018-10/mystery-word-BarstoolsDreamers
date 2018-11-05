import random

print("Welcome to Mystery Word Game!")

print('')

name = input("What is your name?")

print("Hello, " + name, "time to play Mystery Word Game!")

print('')

word_length = 0
word = []
word_status = []
difficulty = (
    input("Would you like to play the easy, normal or hard mode? ")).lower()
easy = [4, 5, 6]
normal = [6, 7, 8]
hard = [9, 10, 11]
if difficulty == "easy":
    word_length = random.choice(easy)
if difficulty == "normal":
    word_length = random.choice(normal)
if difficulty == "hard":
    word_length = random.choice(hard)

with open("words.txt") as words_file:
    for w in words_file.readlines():
        if len(w.strip()) == word_length:
            word.append(w)
chosen_word = (random.choice(word)).lower()

for char in chosen_word.strip():
    word_status.append("_")
print(" ".join(word_status), "Your word contains", word_length, "letters")


def guess(guesses):
    while True:
        print("Guess one letter between a - z.")
        guess = input()
        guess = guess.lower()
        if len(guess) != 1:
            print("Just one letter, please.")
        elif guess in guesses:
            print("You have already guessed that letter.")
        elif guess not in 'abcdefghijklmnopqrstuvwxyz':
            print("Please choose a letter!")
        else:
            return guess

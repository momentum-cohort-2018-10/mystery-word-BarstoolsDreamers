import random

# words = []
# secretWord = random.choice(words.txt)
# length_word = 0
# word_status = []

# welcome the player


def start():
    print("What is your name")
    name = input("What is your name?")


def name():
    print("Hello, " + name, ",", "shall we play a game of mystery word?")

    print(" ")

    print("Hello, " + name, ",", "shall we play a game of mystery word?")

    print(" ")

    print("First, please select a level of difficulty, easy, normal, or hard.")

    print(" ")

# easy = [4, 5, 6]
# normal = [6, 7, 8]
# hard = [9, 10, 11]
# if difficulty == "easy":
#     length_word = random.choice(easy)
# if difficulty == "normal":
#     length_word = random.choice(normal)
# if difficulty == "hard":
#     length_word = random.choice(hard)

# with open("words.txt") as words_file:
#     for w in words_file.readlines():
#         if len(w.strip()) == length_word:
#             word.append(w)
# chosen_word = (random.choice(words)).lower()

# for char in chosen_word.strip():
#     word_status.append("_")
# print(" ".join(word_status), "Your word contains", length_word, "letters")


# def print_instructions():
#     print(
#         "Now, I am going to choose a random word and you will have 8 tries to get it right."
#     )


# print(" ")

# print("Start guessing...")


# def display_letter(letter, guesses):
#     if letter in guesses:
#         return letter
#     else:
#         return "_"


# [letter if letter in guesses else "_"
#  for letter in word]

# def within_range(number, min=None, max=None):
#     """
#     Given a possible minimum and maximum, return True if the number is between
#     the min and max, otherwise return False.
#     """
#     if min is not None and number < min:
#         return False
#     if max is not None and number > max:
#         return False
#     return True


# print("Shall we play?")


# def play_game(min, max):
#     unused_variable = 1
#     print_instructions()
#     number_to_guess = random.randint(min, max)
#     number_guessed = False
#     guesses = 0

#     while not number_guessed and guesses < 10:
#         guess = input_integer("What's your guess? ", min=1, max=1000)
#         guesses += 1
#         if guess == number_to_guess:
#             print("You got it right!")
#             number_guessed = True
#         elif guess < number_to_guess:
#             print("Too low!")
#         else:
#             print("Too high!")


# def print_instructions():
#     print(
#         "I am going to choose a number between 1 and 1000. You have 10 guesses to get it right."
#     )


# def input_integer(prompt, min=None, max=None):
#     """
#     Ask the user for an integer within a range. If invalid input given,
#     keep asking until you get valid input.
#     """
#     guess = input(prompt)
#     while not (is_integer(guess) and within_range(int(guess), min, max)):
#         print("Invalid input")
#         guess = input(prompt)
#     return int(guess)


# def is_integer(string):
#     return string.isdigit()


# def within_range(number, min=None, max=None):
#     """
#     Given a possible minimum and maximum, return True if the number is between
#     the min and max, otherwise return False.
#     """
#     if min is not None and number < min:
#         return False
#     if max is not None and number > max:
#         return False
#     return True


# min = 1
# max = 1000
# play_game(min, max)
# print(random.choice(words))

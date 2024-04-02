import random
import sys


def retrieve_list():
    file = open("./textfiles/words.txt", "r")
    return [word.strip() for word in file.readlines()]


words_list = retrieve_list()


def select_random_word():
    return random.choice(words_list)


def hint(answer: str):
    word = [letter for letter in answer]
    scope = len(word)
    index_of_hint = random.choice(range(scope))

    for index in range(scope):
        if index == index_of_hint:
            continue
        word[index] = "_"
    return word, answer


def start(hidden_word):
    print("can you guess the word : " + "".join(hidden_word))


def print_stick_figure(incorrect_guesses):
    stages = [

        """
           _______
          |       |
          |
          |
          |
          |
        __|__
        """,
        # Stage 1: Head
        """
           _______
          |       |
          |       O
          |
          |
          |
        __|__
        """,

        """
           _______
          |       |
          |       O
          |       |
          |       |
          |
        __|__
        """,

        """
           _______
          |       |
          |       O
          |      /|
          |       |
          |
        __|__
        """,

        """
           _______
          |       |
          |       O
          |      /|\\
          |       |
          |
        __|__
        """,

        """
           _______
          |       |
          |       O
          |      /|\\
          |       |
          |      /
        __|__
        """,

        """
           _______
          |       |
          |       O
          |      /|\\
          |       |
          |      / \\
        __|__
        """
    ]

    print(stages[incorrect_guesses])


generated_hint, answer = hint(select_random_word())

player_guess = ""
turns_taken = 0
incorrect_guess = 0
max_turns = 6


def evaluate(guess):
    found = False

    for index in range(len(answer)):
        if answer[index] == guess and generated_hint[index] == "_":
            generated_hint[index] = guess

            found = True
        elif answer[index] == guess:
            print("you have already found : " + player_guess)

    if "".join(generated_hint) == answer:
        print(f"you win it took {turns_taken} turn(s).")
        sys.exit(0)

    if not found:
        print("incorrect")
        return 1
    print("correct")
    return 0


while turns_taken <= max_turns:
    start(generated_hint)
    player_guess = input()
    turns_taken += 1

    if len(player_guess) > 6:

        if player_guess == answer:
            print("correct it took this amount of turns : " + str(turns_taken))
            break
        else:
            print_stick_figure(6)
            print("Incorrect guess , Game over!")
            break
    else:
        incorrect_guess = incorrect_guess + evaluate(player_guess)
        print_stick_figure(incorrect_guess)
        if turns_taken == max_turns:
            print("sorry but you are out of time.")

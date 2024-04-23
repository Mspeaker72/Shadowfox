import random
import sys
import subprocess


def retrieve_list():
    file = open("./textfiles/words.txt", "r")
    return [word.strip() for word in file.readlines()]


def get_user_input():
    while True:
        player_input = input("Please enter your guess below : \n").lower()

        if len(player_input) == 1 or len(player_input) == len(answer):
            return player_input
        else:
            print("Please enter a single character or word the same length as the hint.")


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
    if state == "":
        print("can you guess the word : " + "".join(hidden_word))
        return

    print(state + " , can you guess the word : " + "".join(hidden_word))


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

state = ""
player_guess = ""
turns_taken = 0
incorrect_guess = 0
max_turns = len(answer)*2


def play_again():
    prompt = input("would you like to play again \n").lower()
    if prompt == "yes":
        subprocess.run(["python", "main.py"])
    else:
        print("thanks for playing.")
        sys.exit(0)


def evaluate(guess):
    global state
    found = False

    for index in range(len(answer)):
        if answer[index] == guess and generated_hint[index] == "_":
            generated_hint[index] = guess

            found = True
        elif answer[index] == guess:
            state = "you have already found : " + player_guess

    if "".join(generated_hint) == answer:
        print(f"you win it took {turns_taken} turn(s) , the word was {answer}")
        play_again()

    if not found:
        if state == "you have already found : " + player_guess:
            return 1

        state = "incorrect"
        return 1

    state = "correct"
    return 0


while turns_taken <= max_turns:
    start(generated_hint)
    player_guess = get_user_input()
    turns_taken += 1

    if len(player_guess) > 1:

        if player_guess == answer:
            print("correct it took this amount of turns : " + str(turns_taken))
            break
        else:
            print_stick_figure(6)
            print("Incorrect guess , Game over! , the word was " + answer)
            break
    else:
        incorrect_guess = incorrect_guess + evaluate(player_guess)
        print_stick_figure(incorrect_guess)
        if incorrect_guess ==6:
            print("sorry but you are out of guesses the word was " + answer)
            break

play_again()
sys.exit(0)

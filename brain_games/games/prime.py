from random import randint
import math

GAME_RULES = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def is_prime(number):
    if number <= 1:
        return False
    for _ in range(2, (int(math.sqrt(number)) + 1)):
        if number % _ == 0:
            return False
    return True


def game_data():
    math_question = randint(2, 100)
    if is_prime(math_question):
        correct_answer = 'yes'
    else:
        correct_answer = 'no'
    return math_question, correct_answer

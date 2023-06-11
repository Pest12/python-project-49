from random import randint
import math

game_rules = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def is_prime(random_number):
    random_number_sqrt = int(math.sqrt(random_number))
    divisors = range(2, (random_number_sqrt + 1))
    for numbers in divisors:
        if random_number % numbers == 0:
            return False
    return True


def game_data():
    math_question = randint(2, 100)
    if is_prime(math_question):
        correct_answer = 'yes'
    else:
        correct_answer = 'no'
    return math_question, correct_answer

from random import randint

GAME_RULES = 'Find the greatest common divisor of given numbers.'


def get_gcd(num_1, num_2):
    while num_1 != num_2:
        if num_1 > num_2:
            num_1 = num_1 - num_2
        else:
            num_2 = num_2 - num_1
    return str(num_2)


def game_data():
    num_1 = randint(1, 100)
    num_2 = randint(1, 100)
    math_question = f'{num_1} {num_2}'
    correct_answer = get_gcd(num_1, num_2)
    return math_question, correct_answer

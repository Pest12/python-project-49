from random import randint

game_rules = 'Find the greatest common divisor of given numbers.'


def game_data():
    num_1 = randint(1, 100)
    num_2 = randint(1, 100)
    math_question = f'{num_1} {num_2}'
    while num_1 != num_2:
        if num_1 > num_2:
            num_1 = num_1 - num_2
        else:
            num_2 = num_2 - num_1
    correct_answer = str(num_2)
    return math_question, correct_answer

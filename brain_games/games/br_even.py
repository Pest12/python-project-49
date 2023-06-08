from random import randint

game_rules = 'Answer "yes" if the number is even, otherwise answer "no".'


def game_data():
    math_question = randint(0, 100)
    current_answer = 'yes' if math_question % 2 == 0 else 'no'
    return math_question, current_answer

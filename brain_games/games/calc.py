from random import randint, choice

GAME_RULES = 'What is the result of the expression?'


def game_data():
    operators = ["-", "+", "*"]
    operator = choice(operators)
    num_1 = randint(0, 30)
    num_2 = randint(0, 30)
    math_question = f'{num_1} {operator} {num_2}'
    if operator == "-":
        correct_answer = num_1 - num_2
    elif operator == "+":
        correct_answer = num_1 + num_2
    elif operator == "*":
        correct_answer = num_1 * num_2
    return math_question, str(correct_answer)

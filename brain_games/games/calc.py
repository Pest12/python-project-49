from random import randint, choice

GAME_RULES = 'What is the result of the expression?'


def game_data():
    operator = ["-", "+", "*"]
    oper = choice(operator)
    num_1 = randint(0, 30)
    num_2 = randint(0, 30)
    math_question = f'{num_1} {oper} {num_2}'
    if oper == "-":
        correct_answer = str(num_1 - num_2)
    elif oper == "+":
        correct_answer = str(num_1 + num_2)
    elif oper == "*":
        correct_answer = str(num_1 * num_2)
    return math_question, correct_answer

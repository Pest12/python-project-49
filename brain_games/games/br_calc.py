from random import randint, choice

game_rules = 'What is result of the expression?'


def game_data():
    operator = ["-", "+", "*"]
    oper = choice(operator)
    num_1 = randint(0, 30)
    num_2 = randint(0, 30)
    math_question = f'{num_1} {oper} {num_2}'
    current_answer = str(eval(math_question))
    return math_question, current_answer

import random

game_rules = 'What number is missing in the progression?'


def game_data():
    progression = []
    start_of_progression = random.randint(0, 20)
    end_of_progression = random.randint(70, 100)
    progression_step = random.randint(1, 5)
    for numbers in range(start_of_progression, end_of_progression, progression_step):
        progression.append(numbers)
    progression_length = slice(random.randint(5, 10))
    hidden_number = random.choice(progression[progression_length])
    correct_answer = str(hidden_number)
    math_question = " ".join(map(str, progression[progression_length]))
    math_question = math_question.replace(correct_answer, '..')
    return math_question, correct_answer

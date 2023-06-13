import random

game_rules = 'What number is missing in the progression?'


def game_data():
    progression = []
    start_of_progression = random.randint(1, 20)
    end_of_progression = random.randint(70, 100)
    progression_step = random.randint(1, 5)
    for numbers in range(start_of_progression,
                         end_of_progression,
                         progression_step):
        progression.append(numbers)
    progression_length = slice(random.randint(5, 10))
    progression_list = progression[progression_length]
    hidden_number = random.choice(progression_list)
    correct_answer = str(hidden_number)
    math_question = " ".join(map(str, progression_list))
    math_question = math_question.replace(correct_answer, '..', 1)
    return math_question, correct_answer

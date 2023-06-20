from random import randint

GAME_RULES = 'What number is missing in the progression?'


def generate_progression():
    progression = []
    start_of_progression = randint(1, 20)
    end_of_progression = randint(70, 100)
    progression_step = randint(1, 5)
    for numbers in range(start_of_progression,
                         end_of_progression,
                         progression_step):
        progression.append(numbers)
    progression_length = slice(randint(5, 10))
    edited_progression = progression[progression_length]
    return edited_progression


def game_data():
    progression = generate_progression()
    hidden_number = randint(0, len(progression) - 1)
    correct_answer = progression[hidden_number]
    progression[hidden_number] = '..'
    math_question = " ".join(map(str, progression))
    return math_question, str(correct_answer)

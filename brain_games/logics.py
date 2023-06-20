import prompt

NUMBER_OF_ROUNDS = 3


def start(game):
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    print(game.GAME_RULES)
    for _ in range(NUMBER_OF_ROUNDS):
        math_question, correct_answer = game.game_data()
        print(f'Question: {math_question}')
        user_answer = prompt.string('Your answer: ')
        if user_answer == correct_answer:
            print('Correct!')
        else:
            print(f"'{user_answer}' is wrong answer ;(."
                  f" Correct answer was '{correct_answer}'.")
            return print(f"Let's try again, {name}!")
    return print(f"Congratulations, {name}!")

import prompt


def start_game(game):
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    print(game.game_rules)
    current_round = 1
    last_round = 3
    while current_round <= last_round:
        math_question, correct_answer = game.game_data()
        print(f'Question: {math_question}')
        user_answer = prompt.string('Your answer: ')
        if user_answer == correct_answer:
            print('Correct!')
        else:
            print(f"'{user_answer}' is wrong answer ;(. Correct answer was '{correct_answer}'.")
            return f"Let's try again, {name}!"
        current_round += 1
    return print(f"Congratulations, {name}!")

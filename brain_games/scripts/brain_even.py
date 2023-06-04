#!/usr/bin/env python3
import prompt
from random import randint


def brain_even():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    print('Answer "yes" if the number is even, otherwise answer "no".')
    i = 1
    wrong_answer = f"Let's try again, {name}!"
    while i <= 3:
        random_number = randint(1, 100)
        print(f'Question: {random_number}')
        print('Your answer: ', end = '')
        answer = input()
        if (answer == 'yes' and random_number % 2 == 0) or (answer == 'no' and random_number % 2 != 0):
            print('Correct!')
        elif answer != 'no' and random_number % 2 != 0:
            print(f"{answer} is wrong answer ;(. Correct answer was 'no'.")
            return print(wrong_answer)
        elif answer != 'yes' and random_number % 2 == 0:
            print(f"{answer} is wrong answer ;(. Correct answer was 'yes'.")
            return print(wrong_answer)
        i += 1
    print(f'Congratulations, {name}!')


def main():
    brain_even()


if __name__ == '__main__':
    main()

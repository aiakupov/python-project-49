#!/usr/bin/env python3
import prompt
import random
from brain_games.scripts.brain_models import *


def greet():
    print('Welcome to the Brain Games!')


def welcome_user():
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    return name


def body():
    print('Answer "yes" if the number is even, otherwise answer "no".')
    counter_right_answer = 0
    while counter_right_answer < 3:
        rand_value = random.randint(1, 100)
        answer = ask_question(f'Question: {rand_value}', 'Your answer: ')
        even = 'no' if rand_value % 2 else 'yes'
        check_condition(even, answer)
        counter_right_answer += 1


def main():
    greet()
    user_name = welcome_user()
    body()
    finish(user_name)


if __name__ == '__main__':
    main()

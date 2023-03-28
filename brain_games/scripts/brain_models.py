#!/usr/bin/env python3
import prompt


def greet():
    print('Welcome to the Brain Games!')


def welcome_user():
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    return name


def check_condition(condition, answer, user_name):
    if condition == answer:
        print('Correct!')
        return True
    else:
        print(f"'{answer}' is wrong answer ;(. Correct answer was '{condition}'.")
        fail(user_name)
        return False


def fail(user_name):
    print(f"Let's try again, {user_name}!")
    exit()


def finish(user_name):
    print(f'Congratulations, {user_name}!')

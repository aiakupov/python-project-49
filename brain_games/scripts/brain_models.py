#!/usr/bin/env python3
import prompt
import random


def greet():
    print('Welcome to the Brain Games!')


def welcome_user():
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    return name


def ask_question(question, answer):
    print(question)
    return prompt.string(answer)


def check_condition(condition, answer):
    if condition == answer:
        print('Correct!')
    else:
        print("'yes' is wrong answer ;(. Correct answer was 'no'.")
        exit()


def finish(user_name):
    print(f'Congratulations, {user_name}!')

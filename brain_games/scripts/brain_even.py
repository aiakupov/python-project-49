#!/usr/bin/env python3
import prompt
import random


def greet():
    print('Welcome to the Brain Games!')


def welcome_user():
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    return name


def ask_question(user_name):
    print('Answer "yes" if the number is even, otherwise answer "no".')
    counter_right_answer = 0
    while counter_right_answer < 3:
        rand_value = random.randint(1, 100)
        print(f'Question: {rand_value}')
        answer = prompt.string('Your answer: ')

        even = 'no' if rand_value % 2 else 'yes'
        if answer == even:
            print('Correct!')
        else:
            print("'yes' is wrong answer ;(. Correct answer was 'no'.")
            exit()
        counter_right_answer += 1

    print(f'Congratulations, {user_name}!')


def main():
    greet()
    user_name = welcome_user()
    ask_question(user_name)


if __name__ == '__main__':
    main()

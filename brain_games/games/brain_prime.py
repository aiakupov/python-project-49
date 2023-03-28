#!/usr/bin/env python3
import random
from brain_games.scripts.brain_models import *


def body(user_name):
    print('Answer "yes" if given number is prime. Otherwise answer "no".')
    counter_right_answer = 0
    while counter_right_answer < 3:
        rand_value = random.randint(1, 100)

        condition = 'yes'
        for number in range(2, rand_value):
            if (rand_value % number) == 0:
                condition = 'no'

        print(f'Question: {rand_value}')
        answer = prompt.string('Your answer: ')
        check_condition(str(condition), str(answer), user_name)

        counter_right_answer += 1


def main():
    greet()
    user_name = welcome_user()
    body(user_name)
    finish(user_name)


if __name__ == '__main__':
    main()

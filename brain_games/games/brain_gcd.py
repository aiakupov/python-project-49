#!/usr/bin/env python3
import random
import math
import prompt
from brain_games.scripts.brain_models \
    import greet, welcome_user, check_condition, finish


def body(user_name):
    print('Find the greatest common divisor of given numbers.')
    counter_right_answer = 0
    while counter_right_answer < 3:
        first_value = random.randint(1, 100)
        second_value = random.randint(1, 100)

        print(f'Question: {first_value} {second_value}')
        answer = prompt.integer('Your answer: ')

        condition = math.gcd(first_value, second_value)
        check_condition(int(condition), int(answer), user_name)

        counter_right_answer += 1


def main():
    greet()
    user_name = welcome_user()
    body(user_name)
    finish(user_name)


if __name__ == '__main__':
    main()

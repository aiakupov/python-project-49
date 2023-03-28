#!/usr/bin/env python3
import random
from brain_games.scripts.brain_models import *


def body(user_name):
    print('What number is missing in the progression?')
    counter_right_answer = 0
    while counter_right_answer < 3:
        rand_value = random.randint(1, 100)
        diff = random.randint(1, 10)
        hidden_index = random.randint(0, 9)

        list_values = []
        for i in range(0, 10):
            list_values.append(rand_value)
            rand_value += diff
        condition = list_values[hidden_index]
        list_values[hidden_index] = '..'

        print('Question:', *list_values)
        answer = prompt.integer('Your answer: ')
        check_condition(int(condition), int(answer), user_name)

        counter_right_answer += 1


def main():
    greet()
    user_name = welcome_user()
    body(user_name)
    finish(user_name)


if __name__ == '__main__':
    main()

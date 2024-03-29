#!/usr/bin/env python3
import random
import prompt
from brain_games.scripts.brain_models \
    import greet, welcome_user, check_condition, finish


def body(user_name):
    print('What is the result of the expression?')
    counter_right_answer = 0
    while counter_right_answer < 3:
        ops = ['+', '-', '*']
        first_operand = random.randint(1, 100)
        second_operand = random.randint(1, 100)
        op = random.choice(ops)
        print(f'Question: {first_operand} {op} {second_operand}')
        answer = prompt.integer('Your answer: ')

        if op == '+':
            condition = first_operand + second_operand
        elif op == '-':
            condition = first_operand - second_operand
        else:
            condition = first_operand * second_operand

        check_condition(int(condition), int(answer), user_name)

        counter_right_answer += 1


def main():
    greet()
    user_name = welcome_user()
    body(user_name)
    finish(user_name)


if __name__ == '__main__':
    main()

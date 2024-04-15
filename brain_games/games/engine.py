import prompt
import operator
import random
from brain_games.games import my_math


def even(user):
    print('Answer "yes" if the number is even, otherwise answer "no".')
    for i in range(0, 3):
        number = random.randint(0, 100)
        print(f'Question: {number}')
        answer = prompt.string('Your answer: ')
        correct_answer = my_math.is_even(number)
        if answer.lower() == str(correct_answer):
            print('Correct!')
        else:
            print(f"Incorrect\nLet's try again, {user}!")
            break
            return None
    print(f'Congratulations, {user}!')


def calc(user):
    operators = {
        "+": operator.add,
        "-": operator.sub,
        "*": operator.mul
    }
    keys = list(operators)
    print('What is the result of the expression?')
    for i in range(0, 3):
        picked_operator = random.choice(keys)
        number_1 = random.randint(0, 100)
        number_2 = random.randint(0, 100)
        print(f'Question: {number_1} {picked_operator} {number_2}')
        answer = prompt.string('Your answer: ')
        corretct_answer = operators[picked_operator](number_1, number_2)
        if answer == str(corretct_answer):
            print('Correct!')
        else:
            print(f"'{answer}' is wrong answer ;(. "
                  f"Correct answer was '{corretct_answer}'."
                  f"\nLet's try again, {user}!")
            break
            return None
    print(f'Congratulations, {user}!')


def gcd(user):
    print('Find the greatest common divisor of given numbers.')
    for i in range(0, 3):
        number_1 = random.randint(0, 100)
        number_2 = random.randint(0, 100)
        print(f'Question: {number_1} {number_2}')
        answer = prompt.string('Your answer: ')
        corretct_answer = my_math.my_gcd(number_1, number_2)
        if answer == str(corretct_answer):
            print('Correct!')
        else:
            print(f"'{answer}' is wrong answer ;(. "
                  f"Correct answer was '{corretct_answer}'."
                  f"\nLet's try again, {user}!")
            break
            return None
    print(f'Congratulations, {user}!')


def progression(user):
    print('What number is missing in the progression?')
    for i in range(0, 3):
        length = random.randint(5, 10)
        g = random.randint(10, 90)
        s = random.randint(1, 10)
        progression = my_math.my_ap(s, g, length)
        v = random.randint(1, len(progression) - 1)
        corretct_answer = progression[v]
        progression[v] = '..'
        li = ' '.join(str(x) for x in progression)
        print(f'Question: {li}')
        answer = prompt.string('Your answer: ')
        if answer == str(corretct_answer):
            print('Correct!')
        else:
            print(f"'{answer}' is wrong answer ;(. "
                  f"Correct answer was '{corretct_answer}'."
                  f"\nLet's try again, {user}!")
            break
            return None
    print(f'Congratulations, {user}!')


def prime(user):
    print('Answer "yes" if given number is prime. Otherwise answer "no".')
    for i in range(0, 3):
        number = random.randint(0, 100)
        print(f'Question: {number}')
        answer = prompt.string('Your answer: ')
        correct_answer = my_math.is_prime(number)
        if answer.lower() == str(correct_answer):
            print('Correct!')
        else:
            print(f"Incorrect\nLet's try again, {user}!")
            break
            return None
    print(f'Congratulations, {user}!')

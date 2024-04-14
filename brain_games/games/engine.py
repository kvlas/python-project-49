import prompt
import operator
import random
import math
from brain_games.scripts import cli
from brain_games.games import my_math

def is_even(user):
    i = 0
    print('Answer "yes" if the number is even, otherwise answer "no".')
    while i < 3:
        number = random.randint(0, 100)
        print(f'Question: {number}')
        answer = prompt.string('Your answer: ')
        if (answer == 'yes' and number % 2 == 0
                or answer == 'no' and number % 2 != 0):
            print('Correct!')
            i += 1
        else:
            print(f"Incorrect\nLet's try again, {user}!")
            i = 0
    print(f'Congratulations, {user}!')


def calc(user):
    i = 0
    operators = {
        "+": operator.add,
        "-": operator.sub,
        "*": operator.mul
    }
    keys = list(operators)
    print('What is the result of the expression?')
    while i < 3:
        picked_operator = random.choice(keys)
        number_1 = random.randint(0, 100)
        number_2 = random.randint(0, 100)
        print(f'Question: {number_1} {picked_operator} {number_2}')
        answer = prompt.string('Your answer: ')
        corretct_answer = operators[picked_operator](number_1, number_2)
        if answer == str(corretct_answer):
            print('Correct!')
            i += 1
        else:
            print(f"'{answer}' is wrong answer ;(. Correct answer was '{corretct_answer}'.\nLet's try again, {user}!")
            i = 0
    print(f'Congratulations, {user}!')


def gcd(user):
    i = 0
    print('Find the greatest common divisor of given numbers.')
    while i < 3:
        number_1 = random.randint(0, 100)
        number_2 = random.randint(0, 100)
        print(f'Question: {number_1}  {number_2}')
        answer = prompt.string('Your answer: ')
        corretct_answer = my_math.my_gcd(number_1, number_2)
        if answer == str(corretct_answer):
            print('Correct!')
            i += 1
        else:
            print(f"'{answer}' is wrong answer ;(. Correct answer was '{corretct_answer}'.\nLet's try again, {user}!")
            i = 0
    print(f'Congratulations, {user}!')


def progression(user):    
    i = 0
    print('What number is missing in the progression?')
    while i < 3:
        l = random.randint(5, 10)
        g = random.randint(10,90)
        s = random.randint(1,10)
        progression = my_math.my_ap(s, g, l)
        v = random.randint(1,len(progression) - 1)
        corretct_answer = progression[v]
        progression[v] = '..'
        li = ' '.join(str(x) for x in progression)
        print(f'Question: {li}')
        answer = prompt.string('Your answer: ')
        if answer == str(corretct_answer):
            print('Correct!')
            i += 1
        else:        
            print(f"'{answer}' is wrong answer ;(. Correct answer was '{corretct_answer}'.\nLet's try again, {user}!")
            i = 0
    print(f'Congratulations, {user}!')


def prime(user):
    i = 0
    print('Answer "yes" if given number is prime. Otherwise answer "no".')
    while i < 3:
        number = random.randint(0, 100)
        print(f'Question: {number}')
        answer = prompt.string('Your answer: ')
        if (answer == 'yes' and my_math.is_prime(number) == True
                or answer == 'no' and my_math.is_prime(number) == False):
            print('Correct!')
            i += 1
        else:
            print(f"Incorrect\nLet's try again, {user}!")
            i = 0
    print(f'Congratulations, {user}!')
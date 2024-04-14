import prompt
import operator
import random
from brain_games.scripts import cli


def odd_or_even(user):
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
    print(f'Congratulations, {user}')


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
        corrtct_answer = operators[picked_operator](number_1, number_2)
        if answer == str(corrtct_answer):
            print('Correct!')
            i += 1
        else:
            print(f"'145' is wrong answer ;(. Correct answer was '{corrtct_answer}'.\nLet's try again, {user}!")
            i = 0
    print(f'Congratulations, {user}')
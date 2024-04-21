import random
from brain_games.games import my_math


def task():
    task = 'Answer "yes" if the number is even, otherwise answer "no".'
    return task


def run():
    number = random.randint(0, 100)
    question = f'Question: {number}'
    correct_answer = my_math.is_even(number)
    return {'question': question, 'correct_answer': correct_answer}

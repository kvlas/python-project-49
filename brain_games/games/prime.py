import random
from brain_games.games import my_math


def task():
    task = 'Answer "yes" if given number is prime. Otherwise answer "no".'
    return task


def run():
    number = random.randint(0, 100)
    question = f'Question: {number}'
    correct_answer = my_math.is_prime(number)
    return {'question': question, 'correct_answer': correct_answer}

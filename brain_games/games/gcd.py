import random
from brain_games.games import my_math


def task():
    task = 'Find the greatest common divisor of given numbers.'
    return task


def run():
    number_1 = random.randint(0, 100)
    number_2 = random.randint(0, 100)
    question = f'Question: {number_1} {number_2}'
    correct_answer = my_math.my_gcd(number_1, number_2)
    return {'question': question, 'correct_answer': correct_answer}

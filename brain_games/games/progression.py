import random
from brain_games.games import my_math


def task():
    task = 'What number is missing in the progression?'
    return task


def run():
    length = random.randint(5, 10)
    g = random.randint(10, 90)
    s = random.randint(1, 10)
    progression = my_math.my_ap(s, g, length)
    v = random.randint(1, len(progression) - 1)
    correct_answer = progression[v]
    progression[v] = '..'
    li = ' '.join(str(x) for x in progression)
    question = f'Question: {li}'
    return {'question': question, 'correct_answer': correct_answer}

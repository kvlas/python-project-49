import random


def task():
    task = 'Answer "yes" if the number is even, otherwise answer "no".'
    return task


def run():
    number = random.randint(0, 100)
    question = f'Question: {number}'
    correct_answer = 'yes' if is_even(number) else 'no'
    return {'question': question, 'correct_answer': correct_answer}


def is_even(digit: int):
    if (digit % 2) == 0:
        return True
    else:
        return False

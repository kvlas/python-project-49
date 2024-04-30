import random


def task():
    task = 'Answer "yes" if given number is prime. Otherwise answer "no".'
    return task


def run():
    number = random.randint(0, 100)
    question = f'Question: {number}'
    correct_answer = 'yes' if is_prime(number) else 'no'
    return {'question': question, 'correct_answer': correct_answer}


def is_prime(digit: int):
    if digit < 2:
        return 'no'
    for i in range(2, int(digit ** 0.5 + 1)):
        if digit % i == 0:
            return False
    else:
        return True

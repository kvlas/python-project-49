import random


def task():
    task = 'Find the greatest common divisor of given numbers.'
    return task


def run():
    number_1 = random.randint(0, 100)
    number_2 = random.randint(0, 100)
    question = f'Question: {number_1} {number_2}'
    correct_answer = str(gcd(number_1, number_2))
    return {'question': question, 'correct_answer': correct_answer}


def gcd(digit_1: int, digit_2: int):
    while digit_1 != digit_2:
        if digit_1 > digit_2:
            digit_1 -= digit_2
        else:
            digit_2 -= digit_1
    return digit_2

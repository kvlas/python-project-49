import operator
import random


def task():
    task = 'What is the result of the expression?'
    return task


def run():
    operators = {
        "+": operator.add,
        "-": operator.sub,
        "*": operator.mul
    }
    keys = list(operators)
    picked_operator = random.choice(keys)
    number_1 = random.randint(0, 100)
    number_2 = random.randint(0, 100)
    question = f'Question: {number_1} {picked_operator} {number_2}'
    correct_answer = operators[picked_operator](number_1, number_2)
    return {'question': question, 'correct_answer': correct_answer}

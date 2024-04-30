import random


def task():
    task = 'What number is missing in the progression?'
    return task


def run():
    length = random.randint(5, 10)
    step = random.randint(10, 90)
    start = random.randint(1, 10)
    progression = generate_progression(start, step, length)
    value = random.randint(1, len(progression) - 1)
    correct_answer = str(progression[value])
    progression[value] = '..'
    new_progression = ' '.join(str(x) for x in progression)
    question = f'Question: {new_progression}'
    return {'question': question, 'correct_answer': correct_answer}


def generate_progression(start: int, step: int, length: int):
    current_vaule = start
    progression = []
    for i in range(1, length + 1):
        current_vaule += step
        progression.append(current_vaule)
    return progression

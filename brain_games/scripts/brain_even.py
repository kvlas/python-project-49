import random
import prompt
from . import cli


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


def main():
    print('Welcome to the Brain Games!')
    cli.welcome_user()
    odd_or_even(cli.user_name)


if __name__ == '__main__':
    main()

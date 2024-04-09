import prompt


def welcome_user():
    global user_name
    user_name = prompt.string('May I have your name? ')
    print(f'Hello, {user_name}!')

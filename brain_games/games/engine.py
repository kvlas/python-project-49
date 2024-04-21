import prompt
import importlib


def start(game_name, user, rounds=3):
    full_module_name = "brain_games.games." + game_name
    game = importlib.import_module(full_module_name)
    print(game.task())
    for i in range(0, rounds):
        x = game.run()
        print(x['question'])
        answer = prompt.string('Your answer: ')
        if answer == str(x['correct_answer']):
            print('Correct!')
        else:
            print(f"'{answer}' is wrong answer ;(. "
                  f"Correct answer was '{x['correct_answer']}'."
                  f"\nLet's try again, {user}!")
            break
            return None
    if i == (rounds - 1):
        print(f'Congratulations, {user}!')

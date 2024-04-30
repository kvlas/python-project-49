import prompt
import importlib


def start(game_name: str, user: str, rounds=3):
    full_module_name = "brain_games.games." + game_name
    picked_game = importlib.import_module(full_module_name)
    print(picked_game.task())
    for i in range(0, rounds):
        game = picked_game.run()
        print(game['question'])
        answer = prompt.string('Your answer: ')
        if answer == game['correct_answer']:
            print('Correct!')
        else:
            print(f"'{answer}' is wrong answer ;(. "
                  f"Correct answer was '{game['correct_answer']}'."
                  f"\nLet's try again, {user}!")
            break
            return None
    if i == (rounds - 1):
        print(f'Congratulations, {user}!')

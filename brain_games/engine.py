import prompt


def start(picked_game, user: str, rounds=3):
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
    if i == (rounds - 1):
        print(f'Congratulations, {user}!')

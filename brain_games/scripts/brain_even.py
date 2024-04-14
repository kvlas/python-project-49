#!/usr/bin/env python3
from brain_games.scripts import cli
from brain_games.games import engine


def main():
    print('Welcome to the Brain Games!')
    cli.welcome_user()
    engine.odd_or_even(cli.user_name)


if __name__ == '__main__':
    main()

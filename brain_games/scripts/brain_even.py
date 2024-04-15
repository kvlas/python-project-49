#!/usr/bin/env python3
from brain_games.scripts import cli
from brain_games.games import engine


def main():
    engine.even(cli.welcome_user())


if __name__ == '__main__':
    main()

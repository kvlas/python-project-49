#!/usr/bin/env python3

from brain_games.scripts import cli
from brain_games import engine
from brain_games.games import even

def main():
    engine.start(even, cli.welcome_user())


if __name__ == '__main__':
    main()

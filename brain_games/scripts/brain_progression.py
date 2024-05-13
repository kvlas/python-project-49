#!/usr/bin/env python3

from brain_games.scripts import cli
from brain_games import engine
from brain_games.games import progression

def main():
    engine.start(progression, cli.welcome_user())


if __name__ == '__main__':
    main()

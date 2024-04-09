# Makefile
install: # deps install
	poetry install

lint: #project linter check
	poetry run flake8 brain_games

build: # Build project
	poetry build

publish: #
	poetry publish --dry-run

package-install: #
	python3 -m pip install --user dist/*.whl

brain-games: # Run project
	poetry run brain-games

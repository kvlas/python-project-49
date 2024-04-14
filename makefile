# Makefile
install: # deps install
	poetry install

lint: #project linter check
	poetry run flake8 brain_games

build: # Build project
	poetry build

publish: # Publish package
	poetry publish --dry-run

package-install: # Install package
	python3 -m pip install --user dist/*.whl

brain-games: # Run project
	poetry run brain-games

brain-even: # Run game even
	poetry run brain-even

brain-calc: # Run game calc
	poetry run brain-calc

brain-gcd: # Run game calc
	poetry run brain-gcd

brain-progression: # Run game calc
	poetry run brain-progression

brain-prime: # Run game calc
	poetry run brain-prime
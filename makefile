# Makefile
install: # deps install
	poetry install

build: # Build project
	poetry build

publish: #
	poetry publish --dry-run

package-install: #
	python3 -m pip install --user dist/*.whl

brain-games: # Run project
	poetry run brain-games

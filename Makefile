install:
	poerty install

brain-games:
	poetry run brain-games

build:
	poetry build

publish:
	poerty publish --dry-run

package-install:
	python3 -m pip install --user dist/*.whl

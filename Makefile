install:
	poetry install
build:
	poetry build
publish:
	poetry publish --dry-run
package-install:
	pip install --user ~/Projects/python-project-lvl2/dist/*.whl
package-reinstall:
	pip install --user ~/Projects/python-project-lvl2/dist/*.whl --force-reinstall
gendiff:
	poetry run gendiff
lint:
	poetry run flake8 gendiff
test:
	poetry 
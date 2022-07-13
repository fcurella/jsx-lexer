black:
	black --line-length 120 .

isort:
	isort --atomic .

lint: isort black

test:
	coverage run --source=jsx setup.py test

release:
	check-manifest
	rm -rf build dist
	python setup.py sdist bdist_wheel
	twine upload dist/*

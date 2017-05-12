test:
	coverage run --source=jsx setup.py test

release:
	rm -rf build dist
	python setup.py sdist bdist_wheel
	twine upload dist/*

test:
	python manage.py test

watch-tests:
	ls *.py | entr python manage.py test

black:
	black -l 86 $$(find * -name '*.py')

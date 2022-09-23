dev:
	uvicorn carleyfamily.asgi:application

# how do we set the environment to production
test:
	python manage.py test

watch-tests:
	ls *.py | entr python manage.py test

# how do we set the environment to production
production:
	uvicorn carleyfamily.asgi:application

black:
	black -l 86 $$(find * -name '*.py')

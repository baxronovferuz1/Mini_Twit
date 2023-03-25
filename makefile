migrate:
	python3 manage.py migrate


run: migrate
	python3 manage.py runserver 0.0.0.0:8000

test:
	echo "Tests..."

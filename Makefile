mig:
	python3 manage.py makemigrations
	python3 manage.py migrate
run:
	python3 manage.py runserver
save:
	pip freeze > requirements.txt
create:
	python3 manage.py createsuperuser
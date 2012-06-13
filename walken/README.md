Setup
-----

	mkvirtualenv walken
	pip install -r requirements.txt
	./manage.py syncdb
	./manage.py migrate
	./manage.py runserver

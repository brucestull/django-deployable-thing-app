.PHONY: resetdb migrate loaddata setup

resetdb:
	rm -f db.sqlite3
	find . -path "*/migrations/*.py" -not -name "__init__.py" -delete
	find . -path "*/migrations/*.pyc" -delete
	echo "Database and migrations cleared."

migrate:
	python manage.py makemigrations
	python manage.py migrate
	echo "Migrations complete."

loaddata:
	python manage.py loaddata sample_things
	echo "Sample data loaded."

setup: resetdb migrate loaddata
	echo "Database reset, migrated, and sample data loaded."

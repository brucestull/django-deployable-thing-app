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

checkenv:
	@test -f .env || (echo ".env file not found. Please copy .env.example to .env and update it."; exit 1)

createsu: checkenv
	@python manage.py shell -c "import os; \
from dotenv import load_dotenv; \
load_dotenv(); \
from django.contrib.auth import get_user_model; \
User = get_user_model(); \
username = os.environ.get('DJANGO_SU_NAME'); \
email = os.environ.get('DJANGO_SU_EMAIL'); \
password = os.environ.get('DJANGO_SU_PASSWORD'); \
User.objects.filter(username=username).exists() or User.objects.create_superuser(username, email, password)" && \
echo "Superuser created or already exists."

setup: resetdb migrate loaddata createsu
	echo "Database reset, migrated, sample data loaded, and superuser created."

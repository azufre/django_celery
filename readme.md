#To start the project

python manage.py runserver

#To apply migrations

python manage.py makemigrations
python manage.py migrate

#To start celery worker

celery -A django_celery worker -l INFO

#To start rabbitmq server 

docker run -d --hostname my-rabbit --name my-rabbit -p 8080:15672 -p 5672:5672 rabbitmq:3-management
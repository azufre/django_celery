
from celery import shared_task
from django.contrib.auth.models import User
from django.core.mail import send_mail
from django_celery import settings


@shared_task
def send_emails_users():
    subject = f'Mensaje de prueba'
    message = f'Welcome, this is a test from celery'
    #users = User.objects.all()[:2]
    User.objects.all().delete()
    # for user in users:
    #     print("Enviando..")
    #     send_mail(subject, message, settings.EMAIL_HOST_USER, 
    #     [user.email], fail_silently=False)

    return "Correos enviados"
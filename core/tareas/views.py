import string

from django.contrib.auth.models import User
from django.shortcuts import render
from django.utils.crypto import get_random_string

# Create your views here.


def create_user_random(cantidad):

    for x in range(1, cantidad):

        username = f'username{get_random_string(5, string.ascii_letters)}'
        email = f'{username}@miempresa.com'
        password = get_random_string(50)

        User.objects.create_user(
            username=username,
            email=email,
            password=password
        )

    return f'{x} Usuarios creados correctamentes'

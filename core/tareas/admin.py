from django.contrib import admin
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin
from .tasks import send_emails_users

# Register your models here.
class MyUserAdmin(UserAdmin):

    actions = ['send_emails', ]

    def send_emails(self, request, queryset):

        send_emails_users.delay()

        return True

admin.site.unregister(User)
admin.site.register(User, MyUserAdmin)
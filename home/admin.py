from django.contrib import admin
from .models import People, Account,CheckPeople
# Register your models here.
admin.site.register(People)
admin.site.register(Account)
admin.site.register(CheckPeople)
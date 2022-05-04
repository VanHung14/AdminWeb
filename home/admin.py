from django.contrib import admin
from .models import People, Account, TimeRecord
# Register your models here.
admin.site.register(People)
admin.site.register(Account)
admin.site.register(TimeRecord)
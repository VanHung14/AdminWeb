import datetime

from django.db import models
# Create your models here.
class People(models.Model):
    ID = models.IntegerField(primary_key=True, null=False, default=0)
    Name = models.CharField(max_length=100,null=True)
    Age = models.IntegerField(null=True)
    Gender = models.IntegerField(null=True)
    RFID = models.CharField(max_length=15,null=True)
    RoleID = models.IntegerField(null=True)

class Account(models.Model):
    people = models.OneToOneField(
        People,
        on_delete=models.CASCADE,
        primary_key=True,
        )
    UserName = models.CharField(max_length=100,null=False)
    Password = models.CharField(max_length=100,null=False)

class TimeRecord(models.Model):
    people = models.ForeignKey(People, on_delete=models.CASCADE)
    time = models.DateTimeField(null=False,default=datetime.datetime.now())
    checkFace = models.IntegerField(null=True,default=0)
    checkRFID = models.IntegerField(null=True,default=0)
    # check = models.IntegerField(null=True,default=0)
    ok = models.IntegerField(null=True,default=0)
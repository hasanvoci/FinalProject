from django.db import models
from django.db.models import DO_NOTHING

from user.models import User


class Department(models.Model):
    name = models.CharField(max_length=50, null=True)
    is_deleted = models.BooleanField(default=False)
    def __str__(self):
        return self.name

class Employee(models.Model):
    name = models.CharField(max_length=15, null=True)
    last_name = models.CharField(max_length=15, null=True)
    birth = models.DateTimeField(null=True)
    gender = models.CharField(max_length=15, null=True)
    dateOfHire = models.DateTimeField(null=True)
    department = models.ForeignKey(Department, on_delete=DO_NOTHING, null=True)
    salary = models.IntegerField(null=True)
    img_url = models.CharField(max_length=500, null=True)
    user = models.ForeignKey(User, on_delete=DO_NOTHING, null=True)
    is_deleted = models.BooleanField(default=False)

    def __str__(self):
        return self.name

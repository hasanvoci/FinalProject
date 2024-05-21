from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models import DO_NOTHING
class Role(models.Model):
    role = models.CharField(max_length=100, default='hr')

    def __str__(self):
        return self.role

class User(AbstractUser):
    role = models.ForeignKey(Role, on_delete=DO_NOTHING, null=True)





class Notification(models.Model):
    message = models.CharField(max_length=2000)
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=DO_NOTHING)

    def __str__(self):
        return self.message

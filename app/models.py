from django.db import models
from django.conf import settings


# Create your models here.
class Emails(models.Model):
    title = models.CharField(max_length=150)
    description = models.CharField(max_length=500)
    mail_text = models.TextField()
    time = models.TimeField()
    status = models.BooleanField()
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    class Meta():
        managed = False

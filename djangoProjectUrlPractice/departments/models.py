from django.db import models


class FirstMode(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    username = models.CharField(null=False)
    password = models.CharField(null=False)


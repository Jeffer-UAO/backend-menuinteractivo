from django.db import models


class UserClient(models.Model):
    title = models.CharField(max_length=10)
    password = models.CharField(max_length=100)

    def __str__(self):
        return self.title

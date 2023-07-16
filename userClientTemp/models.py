from django.db import models


class UserClientTemp(models.Model):
    title = models.CharField(max_length=10)

    def __str__(self):
        return self.title

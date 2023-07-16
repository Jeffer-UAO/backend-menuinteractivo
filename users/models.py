from django.db import models
from django.contrib.auth.models import AbstractUser
from simple_history.models import HistoricalRecords


class User(AbstractUser):
    email = models.EmailField(unique=True)
    history = HistoricalRecords()

   # USERNAME_FIELD = 'email'
   # REQUIRED_FIELDS = []

                                                #USERNAME_FIELD = 'username'
                                                #REQUIRED_FIELDS = ['email','name','last_name']

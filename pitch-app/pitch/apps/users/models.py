from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator
from datetime import datetime
from .constants import ROLE_CHOICES


class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    birthday = models.DateField(validators=[MaxValueValidator(datetime.now())])
    role = models.CharField(max_length=250, choices=ROLE_CHOICES)

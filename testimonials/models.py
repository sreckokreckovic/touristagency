from django.db import models
from django.contrib.auth.models import User


class Testimonial(models.Model):
    first_name = models.CharField(max_length=64, default=None)
    last_name = models.CharField(max_length=64, default=None)
    description = models.CharField(max_length=256)


    def __str__(self):
        return self.title

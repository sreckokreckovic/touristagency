from django.db import models
from django.contrib.auth.models import User


class Testimonial(models.Model):

    description = models.CharField(max_length=256)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

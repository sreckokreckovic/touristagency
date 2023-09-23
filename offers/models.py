from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=64)

    def __str__(self):
        return self.name


class Offer(models.Model):
    title = models.CharField(max_length=64)
    description = models.CharField(max_length=256, blank=True)
    price = models.IntegerField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)


class Media(models.Model):
    path = models.ImageField()
    offer = models.ForeignKey(Offer, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

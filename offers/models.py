from django.db import models

class Categories(models.Model):
    name = models.CharField(max_length=64)

    def __str__(self):
        return self.name

class Offers(models.Model):
    title = models.CharField(max_length=64)
    description = models.CharField(max_length=256, blank=True)
    price = models.IntegerField()
    category = models.ForeignKey(Categories, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

from django.db import models

# Create your models here.
class Books(models.Model):
    name = models.CharField(max_length=50)
    author = models.CharField(max_length=50)
    price = models.IntegerField()
    pages = models.IntegerField()
    def __str__(self):
        return self.name
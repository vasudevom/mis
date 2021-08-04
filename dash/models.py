from django.db import models

# Create your models here.


class Progress(models.Model):
    username= models.CharField(max_length=100)
    task= models.CharField(max_length=200)
    report= models.CharField(max_length=100)
    date = models.DateField()

    def __str__(self):
        return self.username
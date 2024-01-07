from django.db import models

class Film(models.Model):
    name = models.CharField(max_length=80)
    gender = models.CharField(max_length=40)
    release_date = models.DateField()
    director = models.CharField(max_length=40)
    actor = models.CharField(max_length=40)
    box_office = models.DecimalField(max_digits=30, decimal_places=2)

    def __str__(self):
        return self.name

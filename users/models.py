from django.db import models


# Create your models here.

class Students(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    address = models.CharField(max_length=100, blank=True, null=True)
    birth_date = models.DateField(blank=True, null=True)
    status = models.BooleanField(default=False)

    def __str__(self):
        return self.name

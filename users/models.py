from django.db import models


# Create your models here.

class Students(models.Model):
    GENDER_CHOICES = (
        ('F', 'Male'),
        ('O', 'Female'),
        ('D', 'Other')
    )
    name = models.CharField(max_length=255, blank=True, null=True)
    address = models.CharField(max_length=100, blank=True, null=True)
    birth_date = models.DateField(blank=True, null=True)
    status = models.BooleanField(default=False)
    gender = models.CharField(
        max_length=1,
        choices=GENDER_CHOICES,
        blank=True,
        null=True
    )

    def __str__(self):
        return self.name


class StudentDetail(models.Model):
    student = models.ForeignKey(
        Students,
        on_delete=models.PROTECT,
        related_name='students'
    )
    document = models.CharField(max_length=100, blank=True, null=True)
    city = models.CharField(max_length=100, blank=True, null=True)

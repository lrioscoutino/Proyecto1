# Generated by Django 3.2.3 on 2023-03-07 00:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_studentdetail'),
    ]

    operations = [
        migrations.AddField(
            model_name='students',
            name='gender',
            field=models.CharField(blank=True, choices=[('M', 'Male'), ('F', 'Female'), ('O', 'Other')], max_length=1, null=True),
        ),
    ]

"""
This models describe the table that stores feedback including gender,months visited and experience
"""

from django.db import models

# Create your models here.

class Client(models.Model):
    id = models.AutoField(primary_key=True)
    gender = models.CharField(max_length=11)
    month = models.CharField(max_length=11)
    experience = models.CharField(max_length=11)

class Meta:
    db_table = 'client'

def __str__(self):
    return f'{self.gender} - {self.month} - {self.experience}'
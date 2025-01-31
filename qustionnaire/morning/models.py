"""
This model describe the table that stores feedback including gender,months visited and experience
"""

from django.db import models

class Feedback(models.Model):
    id = models.AutoField(primary_key=True)

    gender = [
        ('Male', 'Male'),
        ('Female', 'Female')
    ]
    gender = models.CharField(max_length=6, choices=gender, default='Male')
    month = models.CharField(max_length=255, null=True)
    experience = [
        ('4', 'Very Satisfied'),
        ('3', 'Satisfied'),
        ('2', 'Unsatisfied'),
        ('1', 'Very Unsatisfied')
        ]
    experience = models.CharField(max_length=20, choices=experience, default='Satisfied')

class Meta:
    db_table = 'feedback'
def __str__(self):
    return f"{self.gender},{self.month},{self.experience}"

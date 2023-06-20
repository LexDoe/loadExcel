from django.db import models

# Create your models here.

class Student(models.Model):
    name = models.CharField(max_length=50, default='')
    lastName = models.CharField(max_length=50, default='')
    email = models.EmailField(default='')
    phone = models.CharField(max_length=10, default='')
    course = models.CharField(max_length=50, default='')
    teacher = models.CharField(max_length=100, default='')
    score = models.FloatField(max_length=5, default='')


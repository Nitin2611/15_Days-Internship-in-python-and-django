from django.db import models

# Create your models here.

class Student(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    fees = models.IntegerField()

    def __str__(self) :
        return self.first_name


class Faculty(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    salary = models.IntegerField()

    def __str__(self) :
        return self.first_name


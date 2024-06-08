from django.db import models

# Create your models here.

class Employees(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50, unique=True, null=False)
    age = models.IntegerField(null=False)
    salary = models.FloatField(null=False)

    def __str__(self):
        return self.name
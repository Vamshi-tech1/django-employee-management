from django.db import models


class Employee_details(models.Model):
    Employee_name=models.CharField(max_length=200)
    Age=models.BigIntegerField()
    description=models.CharField(max_length=200)
    image=models.ImageField(upload_to='story_image/')


    def __str__(self):
        return self.Employee_name
        

# Create your models here.

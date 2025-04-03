from django.db import models

# Create your models here.
class Users(models.Model):
    name=models.CharField(max_length=50)
    family=models.CharField(max_length=50)
    phone=models.CharField(max_length=50,null=True)
    email=models.CharField(max_length=50 , null=True)
    status=models.BooleanField(default=True)
    is_deleted=models.BooleanField(default=False)
    password=models.CharField(max_length=15)
    class Meta:
        db_table='users'

class Course(models.Model):
    course_name=models.CharField(max_length=50)
    teacher=models.CharField(max_length=50)
    status=models.BooleanField(default=1)
    is_deleted=models.BooleanField(default=False)
    class Meta:
        db_table='course'
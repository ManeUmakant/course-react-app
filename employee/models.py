from django.db import models

# Create your models here.


class Student(models.Model):

    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=50, unique=True)
    address = models.CharField(max_length=250)


    def __str__(self):

        return self.name


    class Meta:
        db_table = 'student'

class Teacher(models.Model):

    name = models.CharField(max_length=50)
    student = models.ForeignKey(Student, on_delete=models.PROTECT)
    email = models.EmailField(max_length=50)
    city = models.CharField(max_length=50)
    gender = models.CharField(max_length=10)
    is_active = models.BooleanField(default=True)

    class Meta:
        db_table = 'teacher'
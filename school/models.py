from django.db import models

# Create your models here.
class Teacher(models.Model):
    name = models.CharField(max_length=100)
    dob = models.DateField()

    def __str__(self):
        return f"Tr. {self.name}"

class Subject(models.Model):
    name = models.CharField(max_length=100)
    grade = models.PositiveIntegerField()
    teacher = models.ManyToManyField(Teacher)

    def __str__(self):
        return f"G{self.grade} - {self.name}"

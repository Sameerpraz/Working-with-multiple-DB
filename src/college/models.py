from django.db import models

# Create your models here.
class Faculty(models.Model):
    name = models.CharField(max_length=50)
    code = models.CharField(max_length=10)
    class Meta:
        app_label = 'college'

    def __str__(self):
        return self.name
    


class Student(models.Model):
    faculty = models.ForeignKey(Faculty, on_delete=models.CASCADE)
    name = models.CharField(max_length=20)
    address = models.CharField(max_length=20)
    class Meta:
        app_label = 'college'
    
    def __str__(self):
        return self.name
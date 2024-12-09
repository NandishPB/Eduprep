from django.db import models

# Create your models here.
class Exam(models.Model):
    name = models.CharField(max_length=200)
    descrption = models.TextField()
    date = models.DateField()

    def __str__(self):
        return self.name

class Resource(models.Model):
    exam = models.ForeignKey(Exam, on_delete=models.CASCADE)
    subject = models.CharField(max_length=200)
    resource_type = models.CharField(max_length=100)
    link = models.URLField()

    def __str__(self):
        return f"{self.subject} ({self.exam.name})"
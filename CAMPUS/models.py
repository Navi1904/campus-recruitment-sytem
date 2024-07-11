# recruitment/models.py

from django.db import models
from django.contrib.auth.models import User

class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    enrollment_number = models.CharField(max_length=20, unique=True)
    department = models.CharField(max_length=50)
    resume = models.FileField(upload_to='resumes/')
    
    def __str__(self):
        return self.user.username

class Company(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    website = models.URLField()
    
    def __str__(self):
        return self.name

class Job(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    description = models.TextField()
    location = models.CharField(max_length=100)
    last_date_to_apply = models.DateField()
    
    def __str__(self):
        return self.title

class Application(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    job = models.ForeignKey(Job, on_delete=models.CASCADE)
    applied_on = models.DateField(auto_now_add=True)
    status = models.CharField(max_length=50, choices=[
        ('applied', 'Applied'),
        ('interview', 'Interview'),
        ('hired', 'Hired'),
        ('rejected', 'Rejected'),
    ], default='applied')
    resume = models.FileField(upload_to='resumes/')
    cover_letter = models.TextField()
    def __str__(self):
        return f"{self.student.user.username} applied to {self.job.title}"

from django.db import models

# Create your models here.

class Department(models.Model):
    name = models.CharField(max_length=100, unique=True)
    image = models.ImageField(upload_to='department_images/', blank=True, null=True)  # New image field

    def __str__(self):
        return self.name

class Project(models.Model):
    title = models.CharField(max_length=200)
    student_name = models.CharField(max_length=100)
    department = models.ForeignKey(Department, on_delete=models.CASCADE, related_name='projects')
    short_description = models.CharField(max_length=300)
    full_description = models.TextField()
    github_or_demo_link = models.URLField(blank=True, null=True)
    hosted_link = models.URLField(blank=True, null=True)  # New field for live/hosted website
    image = models.ImageField(upload_to='project_images/', blank=True, null=True)  # New image field

    def __str__(self):
        return f"{self.title} ({self.student_name})"

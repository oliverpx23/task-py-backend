from django.db import models

# Create your models here.

class AppUser(models.Model):
    name = models.CharField(max_length=100)
    username = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.pk} - {self.username}"


class Task(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    status = models.CharField(max_length=20, default='pending')
    assigned_to = models.ForeignKey(AppUser, related_name='assigned_to', on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.pk} - {self.name}"
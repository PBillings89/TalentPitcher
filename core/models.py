from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


class CV(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)  # Replace `1` with the ID of an existing user
    content = models.TextField()

    def __str__(self):
        return self.owner

class JobPost(models.Model):
    title = models.CharField(max_length=200)
    location = models.CharField(max_length=100, default="N/A")
    salary = models.DecimalField(max_digits=8, decimal_places=2, default=0.0)
    description = models.TextField()
    skills_required = models.TextField(default="N/A")  # Specify a default value for skills_required

    def __str__(self):
        return self.title


class Role(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(blank=True)
    location = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return str(self.user)


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()


class Post(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


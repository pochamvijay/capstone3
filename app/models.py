from django.db import models


class Profile(models.Model):

    name = models.CharField(max_length=100)

    email = models.EmailField()

    mobile = models.CharField(max_length=15)

    degree = models.CharField(max_length=100)

    about = models.TextField()

    university = models.CharField(max_length=100)

    school = models.CharField(max_length=100)

    previous_work = models.CharField(max_length=100)

    skills = models.CharField(max_length=200)
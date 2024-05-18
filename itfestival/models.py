from django.db import models


class Speaker(models.Model):
    name = models.CharField
    information = models.TextField
    photo = models.ImageField

    def __str__(self):
        return self.name


class Sponsors(models.Model):
    name = models.CharField(max_length=255)
    photo = models.ImageField()
    url = models.URLField(max_length=200)

    def __str__(self):
        return self.name


class Partners(models.Model):
    name = models.CharField(max_length=255)
    photo = models.ImageField()
    url = models.URLField(max_length=200)

    def __str__(self):
        return self.name



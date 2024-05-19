from django.db import models
from section.models import Sections
import random


class Members(models.Model):
    name = models.CharField(max_length=225)
    email = models.EmailField(max_length=225, unique=True)
    confirmation_code = models.IntegerField(editable=False)
    accepted = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)
    section = models.ForeignKey(Sections, on_delete=models.CASCADE)

    def save(self, *args, **kwargs):
        if not self.confirmation_code:
            self.confirmation_code = random.randint(100000, 999999)
        super().save(*args, **kwargs)


    def __str__(self):
        return self.name


class Cheks(models.Model):
    inn = models.IntegerField()
    chek = models.ImageField()

    def __str__(self):
        return self.inn


class Translate(models.Model):
    chek = models.ImageField()
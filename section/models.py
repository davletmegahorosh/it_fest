import unidecode
from django.db import models


class Sections(models.Model):
    name = models.CharField(max_length=225)
    description = models.TextField()
    place_1 = models.IntegerField()
    place_2 = models.IntegerField()
    place_3 = models.IntegerField()
    poster = models.ImageField()
    register_price = models.IntegerField()
    mapp = models.FileField()
    path = models.CharField(max_length=225, editable= False, unique=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.link:
            transliterated_name = unidecode(self.name)
            self.link = slugify(transliterated_name)

        super().save(*args, **kwargs)



from django.db import models
from Petstagram.pets.choices import TYPE_CHOICES

# Create your models here.

class Pet(models.Model):

    type = models.CharField(
        max_length=10,
        choices=TYPE_CHOICES,
    )
    name = models.CharField(
        max_length=10,
        null=True,
        blank=True,
    )
    age = models.PositiveIntegerField(
        null=True,
        blank=True,
    )
    description = models.TextField(
        null=True,
        blank=True,
    )
    image = models.ImageField(
        upload_to='pet_photos/',
        # default='default_pics/default.jpg',
    )
    # def __str__(self):
    #     return f'{self.name}, {self.age}, {self.type}'


class Like(models.Model):
    pet = models.ForeignKey(Pet, on_delete=models.CASCADE)
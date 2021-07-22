from django.db import models

# Create your models here.
from Petstagram.pets.models import Pet


class Comment(models.Model):
    text = models.TextField()
    pet = models.ForeignKey(
        Pet,
        on_delete=models.CASCADE,
    )
    # user = models.ForeignKey(
    #     UserModel,
    #     on_delete=models.CASCADE
    # )



# Generated by Django 3.2.4 on 2021-06-10 17:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pets', '0002_remove_pet_image_url'),
    ]

    operations = [
        migrations.AddField(
            model_name='pet',
            name='image_url',
            field=models.URLField(blank=True, null=True),
        ),
    ]

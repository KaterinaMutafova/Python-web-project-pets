# Generated by Django 3.2.4 on 2021-07-22 00:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pets', '0008_alter_pet_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pet',
            name='image',
            field=models.ImageField(upload_to='pet_photos/'),
        ),
    ]

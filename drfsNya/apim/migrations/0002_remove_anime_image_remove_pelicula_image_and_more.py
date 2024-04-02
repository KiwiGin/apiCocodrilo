# Generated by Django 5.0.3 on 2024-04-02 19:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("apim", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="anime",
            name="image",
        ),
        migrations.RemoveField(
            model_name="pelicula",
            name="image",
        ),
        migrations.RemoveField(
            model_name="serie",
            name="image",
        ),
        migrations.AddField(
            model_name="anime",
            name="image_link",
            field=models.CharField(
                default="https://i.imgur.com/2Z2v1ZG.jpg", max_length=255
            ),
        ),
        migrations.AddField(
            model_name="pelicula",
            name="image_link",
            field=models.CharField(
                default="https://i.imgur.com/2Z2v1ZG.jpg", max_length=255
            ),
        ),
        migrations.AddField(
            model_name="serie",
            name="image_link",
            field=models.CharField(
                default="https://i.imgur.com/2Z2v1ZG.jpg", max_length=255
            ),
        ),
    ]

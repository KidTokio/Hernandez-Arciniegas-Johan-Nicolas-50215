# Generated by Django 5.0.2 on 2024-03-26 22:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0005_alter_juego_trailer'),
    ]

    operations = [
        migrations.AlterField(
            model_name='juego',
            name='trailer',
            field=models.FileField(upload_to='media/videos/'),
        ),
    ]

# Generated by Django 3.2.8 on 2021-11-03 18:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('songhub', '0008_song_duration'),
    ]

    operations = [
        migrations.AlterField(
            model_name='song',
            name='created_date',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]

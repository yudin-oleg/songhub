# Generated by Django 3.2.4 on 2021-06-11 21:05

from django.db import migrations
import songhub.models


class Migration(migrations.Migration):

    dependencies = [
        ('songhub', '0004_auto_20210611_2340'),
    ]

    operations = [
        migrations.AlterField(
            model_name='song',
            name='name',
            field=songhub.models.LowerCharField(max_length=15),
        ),
    ]

# Generated by Django 3.2.13 on 2022-06-14 08:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('awardsapp', '0009_auto_20220613_1311'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='contact',
            field=models.PositiveIntegerField(default=0),
        ),
    ]

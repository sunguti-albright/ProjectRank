# Generated by Django 3.2.13 on 2022-06-13 08:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('awardsapp', '0005_alter_profile_avatar'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='author',
            new_name='user',
        ),
    ]

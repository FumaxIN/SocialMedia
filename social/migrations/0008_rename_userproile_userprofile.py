# Generated by Django 4.1.7 on 2023-04-07 10:54

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('social', '0007_userproile'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='UserProile',
            new_name='UserProfile',
        ),
    ]

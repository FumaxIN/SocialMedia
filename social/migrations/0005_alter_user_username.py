# Generated by Django 4.1.7 on 2023-04-07 08:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('social', '0004_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='username',
            field=models.CharField(blank=True, max_length=10),
        ),
    ]

# Generated by Django 4.1.7 on 2023-04-09 11:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('social', '0010_alter_post_media'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='profile_image',
            field=models.ImageField(blank=True, null=True, upload_to='user_image'),
        ),
    ]

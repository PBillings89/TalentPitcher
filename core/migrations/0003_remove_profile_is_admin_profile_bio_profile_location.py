# Generated by Django 4.2.1 on 2023-05-19 21:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_rename_experience_cv_content_remove_cv_owner_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='is_admin',
        ),
        migrations.AddField(
            model_name='profile',
            name='bio',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='location',
            field=models.CharField(blank=True, max_length=255),
        ),
    ]

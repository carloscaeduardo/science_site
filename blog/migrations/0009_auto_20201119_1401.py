# Generated by Django 3.1.2 on 2020-11-19 14:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_auto_20201119_1334'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='header_image',
            field=models.ImageField(blank=True, null=True, upload_to='media/'),
        ),
        migrations.AddField(
            model_name='post',
            name='second_image',
            field=models.ImageField(blank=True, null=True, upload_to='media/'),
        ),
        migrations.AddField(
            model_name='post',
            name='third_image',
            field=models.ImageField(blank=True, null=True, upload_to='media/'),
        ),
        migrations.DeleteModel(
            name='PostImages',
        ),
    ]

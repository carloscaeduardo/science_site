# Generated by Django 3.1.2 on 2020-11-16 22:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_post_slug'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Comment',
        ),
    ]

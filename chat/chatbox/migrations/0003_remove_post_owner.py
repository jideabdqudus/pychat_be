# Generated by Django 3.2.4 on 2021-06-18 13:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('chatbox', '0002_post_owner'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='owner',
        ),
    ]

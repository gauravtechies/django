# Generated by Django 2.0.8 on 2019-06-20 11:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0002_about_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='about',
            name='city',
        ),
    ]

# Generated by Django 4.2.5 on 2023-09-21 12:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reservations', '0001_initial'),
        ('offers', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Categories',
            new_name='Category',
        ),
        migrations.RenameModel(
            old_name='Offers',
            new_name='Offer',
        ),
    ]
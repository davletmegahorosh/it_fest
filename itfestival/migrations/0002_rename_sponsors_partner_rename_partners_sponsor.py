# Generated by Django 5.0.6 on 2024-05-18 21:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('itfestival', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Sponsors',
            new_name='Partner',
        ),
        migrations.RenameModel(
            old_name='Partners',
            new_name='Sponsor',
        ),
    ]

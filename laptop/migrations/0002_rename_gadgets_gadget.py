# Generated by Django 4.0.1 on 2022-01-31 15:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('laptop', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Gadgets',
            new_name='Gadget',
        ),
    ]
# Generated by Django 5.0.6 on 2024-07-06 07:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('authapp', '0003_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='customuser',
            old_name='phone',
            new_name='phonenumber',
        ),
    ]

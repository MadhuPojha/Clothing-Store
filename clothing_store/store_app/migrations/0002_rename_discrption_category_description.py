# Generated by Django 5.0.6 on 2024-05-24 10:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store_app', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='category',
            old_name='discrption',
            new_name='description',
        ),
    ]

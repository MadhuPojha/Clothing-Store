# Generated by Django 5.0.6 on 2024-05-28 12:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user_app', '0004_address_userbillinginfo_usershippinginfo'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userbillinginfo',
            old_name='billing_address',
            new_name='address',
        ),
    ]

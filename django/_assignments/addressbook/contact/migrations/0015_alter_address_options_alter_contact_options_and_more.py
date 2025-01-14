# Generated by Django 4.0.4 on 2022-05-30 15:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0014_alter_address_options_alter_contact_options_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='address',
            options={'default_related_name': 'contact_address', 'verbose_name': 'Address', 'verbose_name_plural': 'Addresses'},
        ),
        migrations.AlterModelOptions(
            name='contact',
            options={'default_related_name': 'contact_contact', 'verbose_name': 'Contact', 'verbose_name_plural': 'Contacts'},
        ),
        migrations.AlterModelOptions(
            name='phone',
            options={'default_related_name': 'contact_phone', 'verbose_name': 'Phone', 'verbose_name_plural': 'Phones'},
        ),
    ]

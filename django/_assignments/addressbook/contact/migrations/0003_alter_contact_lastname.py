# Generated by Django 4.0.4 on 2022-05-30 12:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0002_contact_birthday'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='lastname',
            field=models.CharField(db_index=True, max_length=30, verbose_name='Last Name'),
        ),
    ]
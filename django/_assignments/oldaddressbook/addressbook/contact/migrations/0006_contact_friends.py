# Generated by Django 2.0.6 on 2018-06-13 12:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0005_auto_20180613_1411'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='friends',
            field=models.ManyToManyField(blank=True, default=None, null=True, to='contact.Person', verbose_name='Friends'),
        ),
    ]
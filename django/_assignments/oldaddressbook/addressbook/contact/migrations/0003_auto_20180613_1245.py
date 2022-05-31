# Generated by Django 2.0.6 on 2018-06-13 10:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0002_contact_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('street', models.CharField(blank=True, default=None, max_length=30, null=True, verbose_name='Street')),
                ('house_number', models.IntegerField(blank=True, default=None, null=True, verbose_name='House Number')),
                ('city', models.CharField(blank=True, default=None, max_length=30, null=True, verbose_name='City')),
            ],
            options={
                'verbose_name': 'Address',
                'verbose_name_plural': 'Addresses',
            },
        ),
        migrations.AlterModelOptions(
            name='person',
            options={'verbose_name': 'Person', 'verbose_name_plural': 'People'},
        ),
        migrations.AddField(
            model_name='address',
            name='person',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='contact.Person', verbose_name='Person'),
        ),
    ]
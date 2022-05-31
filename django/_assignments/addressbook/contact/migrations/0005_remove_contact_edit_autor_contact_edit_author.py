# Generated by Django 4.0.4 on 2022-05-30 12:54

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('contact', '0004_contact_add_author_contact_add_date_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contact',
            name='edit_autor',
        ),
        migrations.AddField(
            model_name='contact',
            name='edit_author',
            field=models.ForeignKey(blank=True, default=None, editable=False, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='edit_author', to=settings.AUTH_USER_MODEL, verbose_name='Edit Author'),
        ),
    ]
# Generated by Django 2.1.9 on 2019-06-27 12:36

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0004_auto_20190627_1526'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='published',
            field=models.DateField(blank=True, default=django.utils.timezone.now, null=True, verbose_name='опубликовано'),
        ),
    ]
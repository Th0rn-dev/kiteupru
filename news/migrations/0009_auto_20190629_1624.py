# Generated by Django 2.1.9 on 2019-06-29 13:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0008_auto_20190626_2129'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='ItemNews',
            new_name='New',
        ),
        migrations.RenameField(
            model_name='new',
            old_name='creation_date',
            new_name='created',
        ),
        migrations.RenameField(
            model_name='new',
            old_name='title_news',
            new_name='title',
        ),
    ]

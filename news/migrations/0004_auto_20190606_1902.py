# Generated by Django 2.1.9 on 2019-06-06 16:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0003_auto_20190606_1841'),
    ]

    operations = [
        migrations.AlterField(
            model_name='itemnews',
            name='title_news',
            field=models.CharField(default='', max_length=70),
        ),
    ]
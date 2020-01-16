# Generated by Django 2.2.6 on 2019-10-05 06:32

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0004_auto_20191001_1119'),
    ]

    operations = [
        migrations.AlterField(
            model_name='property',
            name='property_type',
            field=models.CharField(choices=[('For Sale', 'For Sale'), ('For Rent', 'For Rent')], max_length=10, verbose_name='property_type'),
        ),
        migrations.AlterField(
            model_name='property',
            name='published',
            field=models.DateTimeField(verbose_name=datetime.datetime(2019, 10, 5, 6, 32, 12, 38324, tzinfo=utc)),
        ),
    ]

# Generated by Django 2.2.6 on 2019-10-06 12:47

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0011_auto_20191006_1746'),
    ]

    operations = [
        migrations.AlterField(
            model_name='property',
            name='published',
            field=models.DateTimeField(verbose_name=datetime.datetime(2019, 10, 6, 12, 47, 3, 902133, tzinfo=utc)),
        ),
    ]

# Generated by Django 2.0.8 on 2019-05-05 10:53

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('to_do', '0005_auto_20190505_1607'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='last_date',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
    ]

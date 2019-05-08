# Generated by Django 2.0.8 on 2019-04-25 18:06

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('description', models.CharField(blank=True, max_length=1000)),
                ('date_of_creation', models.DateTimeField(default=datetime.datetime.now)),
                ('priority', models.CharField(choices=[('adanger', 'Priority High'), ('bwarning', 'Priority Medium'), ('csuccess', 'Priority Low')], default='adanger', max_length=30)),
                ('complete', models.IntegerField(default=0)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
# Generated by Django 3.2 on 2021-04-21 16:27

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gym', '0002_alter_member_expiredate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='member',
            name='expiredate',
            field=models.DateField(default=datetime.datetime(2021, 5, 21, 22, 12, 8, 315712), max_length=40),
        ),
    ]

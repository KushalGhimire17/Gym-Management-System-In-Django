# Generated by Django 3.2 on 2021-04-15 01:57

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Enquiry',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=60)),
                ('contact', models.CharField(max_length=10)),
                ('emailid', models.CharField(max_length=60)),
                ('age', models.CharField(max_length=40)),
                ('gender', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Equipment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('price', models.CharField(max_length=10)),
                ('unit', models.CharField(max_length=10)),
                ('date', models.CharField(max_length=40)),
                ('description', models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='Member',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, unique=True, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('contact', models.CharField(max_length=10)),
                ('emailid', models.CharField(max_length=50)),
                ('age', models.CharField(max_length=40)),
                ('gender', models.CharField(default='', max_length=10)),
                ('plan', models.CharField(max_length=50)),
                ('joindate', models.DateField(max_length=40)),
                ('expiredate', models.DateField(default=datetime.datetime(2021, 5, 15, 7, 42, 57, 526019), max_length=40)),
                ('initialamount', models.CharField(max_length=10)),
                ('qr_code', models.ImageField(blank=True, upload_to='qr_codes')),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('image', models.ImageField(upload_to='order')),
                ('price', models.DecimalField(decimal_places=2, max_digits=12)),
                ('quantity', models.PositiveIntegerField(default=1)),
            ],
        ),
        migrations.CreateModel(
            name='Plan',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('amount', models.CharField(max_length=10)),
                ('duration', models.CharField(max_length=10)),
            ],
        ),
    ]

# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-07-26 20:17
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('line1', models.CharField(max_length=150)),
                ('line2', models.CharField(max_length=150)),
                ('postalCode', models.CharField(max_length=10)),
                ('city', models.CharField(max_length=150)),
                ('country', models.CharField(max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('adm_date', models.DateTimeField(verbose_name='date published')),
                ('address', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rescue.Address')),
            ],
        ),
    ]
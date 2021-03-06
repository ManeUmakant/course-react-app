# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-02-15 02:49
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0003_auto_20180212_0309'),
    ]

    operations = [
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=50)),
                ('city', models.CharField(max_length=50)),
                ('gender', models.CharField(max_length=10)),
                ('is_active', models.BooleanField(default=True)),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='employee.Student')),
            ],
            options={
                'db_table': 'teacher',
            },
        ),
    ]

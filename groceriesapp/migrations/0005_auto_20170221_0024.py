# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-02-21 00:24
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('groceriesapp', '0004_auto_20170220_2349'),
    ]

    operations = [
        migrations.CreateModel(
            name='TripItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.FloatField(default=0)),
                ('tax', models.FloatField(null=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='item',
            name='store',
        ),
        migrations.RemoveField(
            model_name='trip',
            name='item',
        ),
        migrations.RemoveField(
            model_name='trip',
            name='quantity',
        ),
        migrations.RemoveField(
            model_name='trip',
            name='tax',
        ),
        migrations.AddField(
            model_name='tripitem',
            name='item',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='groceriesapp.Item'),
        ),
        migrations.AddField(
            model_name='tripitem',
            name='trip',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='groceriesapp.Trip'),
        ),
    ]

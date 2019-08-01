# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dataApp', '0003_registration_status'),
    ]

    operations = [
        migrations.CreateModel(
            name='Request',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('rabin', models.CharField(max_length=50)),
                ('userid', models.IntegerField()),
                ('status', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Uploader',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('Filename', models.CharField(max_length=50)),
                ('fingerprint', models.CharField(max_length=100)),
                ('userid', models.IntegerField()),
                ('status', models.IntegerField()),
            ],
        ),
    ]

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dataApp', '0005_remove_request_userid'),
    ]

    operations = [
        migrations.AddField(
            model_name='request',
            name='userid',
            field=models.CharField(default='', max_length=10),
            preserve_default=False,
        ),
    ]

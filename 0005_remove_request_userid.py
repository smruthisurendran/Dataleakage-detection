# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dataApp', '0004_request_uploader'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='request',
            name='userid',
        ),
    ]

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dataApp', '0006_request_userid'),
    ]

    operations = [
        migrations.AddField(
            model_name='request',
            name='checked',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dataApp', '0002_registration_role'),
    ]

    operations = [
        migrations.AddField(
            model_name='registration',
            name='status',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]

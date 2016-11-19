# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('voting', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='choice',
            name='test',
            field=models.CharField(default=None, max_length=40),
            preserve_default=False,
        ),
    ]

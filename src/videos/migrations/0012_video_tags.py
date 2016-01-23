# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('videos', '0011_taggeditem'),
    ]

    operations = [
        migrations.AddField(
            model_name='video',
            name='tags',
            field=models.CharField(max_length=20, null=True, blank=True),
        ),
    ]

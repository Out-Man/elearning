# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('videos', '0014_auto_20150805_2310'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='video',
            options={'ordering': ['order', '-timestamp']},
        ),
    ]

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('videos', '0012_video_tags'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='video',
            name='tags',
        ),
    ]

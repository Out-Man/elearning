# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('videos', '0002_video_active'),
    ]

    operations = [
        migrations.AddField(
            model_name='video',
            name='featured',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='video',
            name='free_preview',
            field=models.BooleanField(default=False),
        ),
    ]

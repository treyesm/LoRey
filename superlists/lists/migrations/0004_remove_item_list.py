# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lists', '0003_auto_20151014_1450'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='item',
            name='list',
        ),
    ]

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ordermgmt', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='master',
            field=models.EmailField(max_length=254),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='orderitem',
            name='user_email',
            field=models.EmailField(max_length=254),
            preserve_default=True,
        ),
    ]

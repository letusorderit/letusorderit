# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone
import model_utils.fields


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(editable=False, default=django.utils.timezone.now, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(editable=False, default=django.utils.timezone.now, verbose_name='modified')),
                ('slug', models.SlugField(unique=True)),
                ('master', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=1000)),
                ('shop_url', models.URLField(blank=True, null=True)),
                ('deadline', models.DateTimeField()),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='OrderItem',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(editable=False, default=django.utils.timezone.now, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(editable=False, default=django.utils.timezone.now, verbose_name='modified')),
                ('slug', models.SlugField(unique=True)),
                ('user_email', models.CharField(max_length=100)),
                ('item_identifier', models.CharField(max_length=100)),
                ('item_url', models.URLField(blank=True, null=True)),
                ('count', models.PositiveSmallIntegerField(default=1)),
                ('amount', models.PositiveIntegerField(blank=True, null=True, help_text='Amount in lowest currency unit.')),
                ('order', models.ForeignKey(to='ordermgmt.Order')),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
    ]

# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-11-09 22:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('abids', '0006_auction_ip'),
    ]

    operations = [
        migrations.AddField(
            model_name='competitor',
            name='bid_ip',
            field=models.GenericIPAddressField(default=0),
            preserve_default=False,
        ),
    ]

# -*- coding: utf-8 -*-
# Generated by Django 1.11.23 on 2019-08-28 17:11
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [("core", "0036_auto_20190828_1709")]

    operations = [
        migrations.AlterField(
            model_name="jobapplication",
            name="challenge_response_at",
            field=models.DateTimeField(blank=True, null=True),
        )
    ]

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0001_initial'),
        ('comments', '0002_auto_20150502_1654'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='infoAuthor',
            field=models.ForeignKey(default=0, to='members.UserInfo'),
            preserve_default=True,
        ),
    ]

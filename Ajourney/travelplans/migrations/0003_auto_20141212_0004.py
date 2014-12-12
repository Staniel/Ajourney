# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('travelplans', '0002_joinedplan'),
    ]

    operations = [
        migrations.CreateModel(
            name='PrivatePlan',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('accessible_plan', models.ForeignKey(to='travelplans.Plan')),
                ('accessible_user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='plan',
            name='is_private',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
    ]

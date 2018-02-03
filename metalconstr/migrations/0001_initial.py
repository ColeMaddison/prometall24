# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('cat_name', models.CharField(max_length=128, unique=True)),
                ('cat_description', models.TextField()),
            ],
            options={
                'db_table': 'category',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Construction',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('const_name', models.CharField(max_length=128)),
                ('const_description', models.TextField()),
                ('const_imagename', models.CharField(max_length=128)),
                ('category', models.ForeignKey(to='metalconstr.Category')),
            ],
            options={
                'db_table': 'construction',
            },
            bases=(models.Model,),
        ),
    ]

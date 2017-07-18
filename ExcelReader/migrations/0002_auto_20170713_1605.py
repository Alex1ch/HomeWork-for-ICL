# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ExcelReader', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='excelentries',
            name='name',
            field=models.CharField(max_length=100, verbose_name='Имя', default='None'),
        ),
    ]

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ExcelEntries',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('name', models.TextField(verbose_name='Имя', default='None')),
                ('desc', models.TextField(verbose_name='Описание', default='None')),
                ('file', models.FileField(upload_to='excel_files', verbose_name='Файл для загрузки')),
            ],
        ),
    ]

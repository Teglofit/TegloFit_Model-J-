# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-10-20 18:58
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('eventoTeglo', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pesagem',
            name='usuario',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Pesagem', to=settings.AUTH_USER_MODEL),
        ),
    ]
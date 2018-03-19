# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-03-19 00:43
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('teams', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Leaderboard',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, help_text='creation date')),
                ('updated_at', models.DateTimeField(auto_now=True, help_text='edition date', null=True)),
                ('points', models.IntegerField(default=0)),
                ('win', models.IntegerField(default=0)),
                ('lose', models.IntegerField(default=0)),
                ('tie', models.IntegerField(default=0)),
                ('team', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='team_leaderboard', to='teams.Team')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2017-05-16 22:32
from __future__ import unicode_literals

import django.core.validators
import django.db.models.deletion
import jsonfield.fields
import morango.utils.uuids
from django.db import migrations
from django.db import models

import kolibri.content.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('exams', '__first__'),
        ('kolibriauth', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='AttemptLog',
            fields=[
                ('id', morango.utils.uuids.UUIDField(editable=False, primary_key=True, serialize=False)),
                ('_morango_dirty_bit', models.BooleanField(default=True, editable=False)),
                ('_morango_source_id', models.CharField(editable=False, max_length=96)),
                ('_morango_partition', models.CharField(editable=False, max_length=128)),
                ('item', models.CharField(max_length=200)),
                ('start_timestamp', models.DateTimeField()),
                ('end_timestamp', models.DateTimeField()),
                ('completion_timestamp', models.DateTimeField(blank=True, null=True)),
                ('time_spent', models.FloatField(default=0.0, help_text='(in seconds)', validators=[django.core.validators.MinValueValidator(0)])),
                ('complete', models.BooleanField(default=False)),
                ('correct', models.FloatField(validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(1)])),
                ('hinted', models.BooleanField(default=False)),
                ('answer', jsonfield.fields.JSONField(blank=True, default={}, null=True)),
                ('simple_answer', models.CharField(blank=True, max_length=200)),
                ('interaction_history', jsonfield.fields.JSONField(blank=True, default=[])),
                ('dataset', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='kolibriauth.FacilityDataset')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ContentSessionLog',
            fields=[
                ('id', morango.utils.uuids.UUIDField(editable=False, primary_key=True, serialize=False)),
                ('_morango_dirty_bit', models.BooleanField(default=True, editable=False)),
                ('_morango_source_id', models.CharField(editable=False, max_length=96)),
                ('_morango_partition', models.CharField(editable=False, max_length=128)),
                ('content_id', kolibri.content.models.UUIDField(db_index=True)),
                ('channel_id', kolibri.content.models.UUIDField()),
                ('start_timestamp', models.DateTimeField()),
                ('end_timestamp', models.DateTimeField(blank=True, null=True)),
                ('time_spent', models.FloatField(default=0.0, help_text='(in seconds)', validators=[django.core.validators.MinValueValidator(0)])),
                ('progress', models.FloatField(default=0, validators=[django.core.validators.MinValueValidator(0)])),
                ('kind', models.CharField(max_length=200)),
                ('extra_fields', jsonfield.fields.JSONField(blank=True, default={})),
                ('dataset', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='kolibriauth.FacilityDataset')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='kolibriauth.FacilityUser')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ContentSummaryLog',
            fields=[
                ('id', morango.utils.uuids.UUIDField(editable=False, primary_key=True, serialize=False)),
                ('_morango_dirty_bit', models.BooleanField(default=True, editable=False)),
                ('_morango_source_id', models.CharField(editable=False, max_length=96)),
                ('_morango_partition', models.CharField(editable=False, max_length=128)),
                ('content_id', kolibri.content.models.UUIDField(db_index=True)),
                ('channel_id', kolibri.content.models.UUIDField()),
                ('start_timestamp', models.DateTimeField()),
                ('end_timestamp', models.DateTimeField(blank=True, null=True)),
                ('completion_timestamp', models.DateTimeField(blank=True, null=True)),
                ('time_spent', models.FloatField(default=0.0, help_text='(in seconds)', validators=[django.core.validators.MinValueValidator(0)])),
                ('progress', models.FloatField(default=0, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(1.01)])),
                ('kind', models.CharField(max_length=200)),
                ('extra_fields', jsonfield.fields.JSONField(blank=True, default={})),
                ('dataset', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='kolibriauth.FacilityDataset')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='kolibriauth.FacilityUser')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ExamAttemptLog',
            fields=[
                ('id', morango.utils.uuids.UUIDField(editable=False, primary_key=True, serialize=False)),
                ('_morango_dirty_bit', models.BooleanField(default=True, editable=False)),
                ('_morango_source_id', models.CharField(editable=False, max_length=96)),
                ('_morango_partition', models.CharField(editable=False, max_length=128)),
                ('item', models.CharField(max_length=200)),
                ('start_timestamp', models.DateTimeField()),
                ('end_timestamp', models.DateTimeField()),
                ('completion_timestamp', models.DateTimeField(blank=True, null=True)),
                ('time_spent', models.FloatField(default=0.0, help_text='(in seconds)', validators=[django.core.validators.MinValueValidator(0)])),
                ('complete', models.BooleanField(default=False)),
                ('correct', models.FloatField(validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(1)])),
                ('hinted', models.BooleanField(default=False)),
                ('answer', jsonfield.fields.JSONField(blank=True, default={}, null=True)),
                ('simple_answer', models.CharField(blank=True, max_length=200)),
                ('interaction_history', jsonfield.fields.JSONField(blank=True, default=[])),
                ('content_id', kolibri.content.models.UUIDField()),
                ('channel_id', kolibri.content.models.UUIDField()),
                ('dataset', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='kolibriauth.FacilityDataset')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ExamLog',
            fields=[
                ('id', morango.utils.uuids.UUIDField(editable=False, primary_key=True, serialize=False)),
                ('_morango_dirty_bit', models.BooleanField(default=True, editable=False)),
                ('_morango_source_id', models.CharField(editable=False, max_length=96)),
                ('_morango_partition', models.CharField(editable=False, max_length=128)),
                ('closed', models.BooleanField(default=False)),
                ('completion_timestamp', models.DateTimeField(blank=True, null=True)),
                ('dataset', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='kolibriauth.FacilityDataset')),
                ('exam', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='examlogs', to='exams.Exam')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='kolibriauth.FacilityUser')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='MasteryLog',
            fields=[
                ('id', morango.utils.uuids.UUIDField(editable=False, primary_key=True, serialize=False)),
                ('_morango_dirty_bit', models.BooleanField(default=True, editable=False)),
                ('_morango_source_id', models.CharField(editable=False, max_length=96)),
                ('_morango_partition', models.CharField(editable=False, max_length=128)),
                ('mastery_criterion', jsonfield.fields.JSONField(default={})),
                ('start_timestamp', models.DateTimeField()),
                ('end_timestamp', models.DateTimeField(blank=True, null=True)),
                ('completion_timestamp', models.DateTimeField(blank=True, null=True)),
                ('mastery_level', models.IntegerField(validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(10)])),
                ('complete', models.BooleanField(default=False)),
                ('dataset', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='kolibriauth.FacilityDataset')),
                ('summarylog', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='masterylogs', to='logger.ContentSummaryLog')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='kolibriauth.FacilityUser')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='UserSessionLog',
            fields=[
                ('id', morango.utils.uuids.UUIDField(editable=False, primary_key=True, serialize=False)),
                ('_morango_dirty_bit', models.BooleanField(default=True, editable=False)),
                ('_morango_source_id', models.CharField(editable=False, max_length=96)),
                ('_morango_partition', models.CharField(editable=False, max_length=128)),
                ('channels', models.TextField(blank=True)),
                ('start_timestamp', models.DateTimeField(auto_now_add=True)),
                ('last_interaction_timestamp', models.DateTimeField(auto_now=True, null=True)),
                ('pages', models.TextField(blank=True)),
                ('dataset', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='kolibriauth.FacilityDataset')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='kolibriauth.FacilityUser')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='examattemptlog',
            name='examlog',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='attemptlogs', to='logger.ExamLog'),
        ),
        migrations.AddField(
            model_name='examattemptlog',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='kolibriauth.FacilityUser'),
        ),
        migrations.AddField(
            model_name='attemptlog',
            name='masterylog',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='attemptlogs', to='logger.MasteryLog'),
        ),
        migrations.AddField(
            model_name='attemptlog',
            name='sessionlog',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='attemptlogs', to='logger.ContentSessionLog'),
        ),
        migrations.AddField(
            model_name='attemptlog',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='kolibriauth.FacilityUser'),
        ),
    ]

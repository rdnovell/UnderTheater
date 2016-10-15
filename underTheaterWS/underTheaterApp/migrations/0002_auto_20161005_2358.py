# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-10-05 23:58
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
        ('underTheaterApp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ticketeable',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('topic', models.CharField(max_length=30)),
                ('polymorphic_ctype', models.ForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='polymorphic_undertheaterapp.ticketeable_set+', to='contenttypes.ContentType')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.RemoveField(
            model_name='dayfunction',
            name='id',
        ),
        migrations.RemoveField(
            model_name='dayfunction',
            name='polymorphic_ctype',
        ),
        migrations.RemoveField(
            model_name='dayfunction',
            name='topic',
        ),
        migrations.RemoveField(
            model_name='playtheater',
            name='id',
        ),
        migrations.RemoveField(
            model_name='playtheater',
            name='polymorphic_ctype',
        ),
        migrations.RemoveField(
            model_name='playtheater',
            name='topic',
        ),
        migrations.AlterField(
            model_name='dayfunction',
            name='play_theater',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='undertheaterapp_dayfunction_related', to='underTheaterApp.PlayTheater', verbose_name='obra'),
        ),
        migrations.AddField(
            model_name='dayfunction',
            name='ticketeable_ptr',
            field=models.OneToOneField(auto_created=True, default=-1, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='underTheaterApp.Ticketeable'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='playtheater',
            name='ticketeable_ptr',
            field=models.OneToOneField(auto_created=True, default=-1, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='underTheaterApp.Ticketeable'),
            preserve_default=False,
        ),
    ]
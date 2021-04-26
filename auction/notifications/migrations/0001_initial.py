# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone
from django.conf import settings
import model_utils.fields


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('contenttypes', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='MailEmployerSettings',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('change_bid', models.BooleanField(default=True, verbose_name='Change bid')),
                ('new_bid', models.BooleanField(default=True, verbose_name='New bid')),
                ('withdraw_bid', models.BooleanField(default=True, verbose_name='Withdraw bid')),
                ('end_tender', models.BooleanField(default=True, verbose_name='End of Tender')),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='MailProviderSettings',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('change_tender', models.BooleanField(default=True, verbose_name='Change in Tender')),
                ('withdraw_tender', models.BooleanField(default=True, verbose_name='Withdraw of Tender')),
                ('end_tender', models.BooleanField(default=True, verbose_name='End of Tender')),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Notification',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, verbose_name='created', editable=False)),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, verbose_name='modified', editable=False)),
                ('unread', models.BooleanField(default=True)),
                ('actor_object_id', models.CharField(max_length=255)),
                ('verb', models.CharField(max_length=255)),
                ('description', models.TextField(blank=True)),
                ('target_object_id', models.CharField(max_length=255, null=True, blank=True)),
                ('action_object_object_id', models.CharField(max_length=255, null=True, blank=True)),
                ('public', models.BooleanField(default=True)),
                ('deleted', models.BooleanField(default=False)),
                ('emailed', models.BooleanField(default=False)),
                ('action_object_content_type', models.ForeignKey(related_name='notify_action_object', blank=True, to='contenttypes.ContentType', null=True)),
                ('actor_content_type', models.ForeignKey(related_name='notify_actor', to='contenttypes.ContentType')),
                ('recipient', models.ForeignKey(related_name='notifications', to=settings.AUTH_USER_MODEL)),
                ('target_content_type', models.ForeignKey(related_name='notify_target', blank=True, to='contenttypes.ContentType', null=True)),
            ],
            options={
                'ordering': ('-created',),
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='NotificationEmployerSettings',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('change_bid', models.BooleanField(default=True, verbose_name='Change bid')),
                ('new_bid', models.BooleanField(default=True, verbose_name='New bid')),
                ('withdraw_bid', models.BooleanField(default=True, verbose_name='Withdraw bid')),
                ('end_tender', models.BooleanField(default=True, verbose_name='End of Tender')),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='NotificationProviderSettings',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('change_tender', models.BooleanField(default=True, verbose_name='Change in Tender')),
                ('withdraw_tender', models.BooleanField(default=True, verbose_name='Withdraw of Tender')),
                ('end_tender', models.BooleanField(default=True, verbose_name='End of Tender')),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
    ]

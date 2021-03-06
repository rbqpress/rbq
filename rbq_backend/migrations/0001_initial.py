# Generated by Django 2.2.5 on 2019-09-18 06:32

from django.conf import settings
import django.contrib.postgres.fields
import django.contrib.postgres.fields.citext
import django.contrib.postgres.fields.jsonb
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.RunSQL(
            "CREATE EXTENSION citext;"
        ),
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('acct', django.contrib.postgres.fields.citext.CITextField(unique=True)),
                ('ap_id', models.TextField(unique=True)),
                ('inbox', models.TextField()),
                ('outbox', models.TextField()),
                ('url', models.TextField()),
                ('is_locked', models.BooleanField(default=False)),
                ('summary', models.TextField(blank=True, default='')),
                ('type', models.CharField(choices=[('Person', 'Person'), ('Service', 'Bot'), ('Group', 'Subforum')], max_length=50)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ASObject',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data', django.contrib.postgres.fields.jsonb.JSONField()),
            ],
        ),
        migrations.CreateModel(
            name='ASActivity',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('data', django.contrib.postgres.fields.jsonb.JSONField()),
                ('domain', models.CharField(max_length=255)),
                ('recipients', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=255), size=None)),
                ('actor', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='activities', to=settings.AUTH_USER_MODEL, to_field='ap_id')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]

# Generated by Django 2.2.5 on 2019-09-19 07:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rbq_backend', '0013_auto_20190918_1222'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='name',
            field=models.TextField(blank=True, default='', null=True),
        ),
        migrations.AlterField(
            model_name='account',
            name='summary',
            field=models.TextField(blank=True, default='', null=True),
        ),
    ]

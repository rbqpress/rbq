# Generated by Django 2.2.5 on 2019-09-18 06:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rbq_backend', '0003_account_email'),
    ]

    operations = [
        migrations.RenameField(
            model_name='account',
            old_name='acct',
            new_name='username',
        ),
    ]

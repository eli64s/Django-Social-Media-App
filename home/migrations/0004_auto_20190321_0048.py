# Generated by Django 2.1.5 on 2019-03-21 00:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_auto_20190321_0046'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='date',
            new_name='created',
        ),
    ]

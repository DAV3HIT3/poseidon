# Generated by Django 3.1 on 2020-08-24 23:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('atlantis', '0015_auto_20200824_2201'),
    ]

    operations = [
        migrations.AlterField(
            model_name='turnerror',
            name='error_msg',
            field=models.CharField(blank=True, default='', max_length=120),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='turnerror',
            name='error_type',
            field=models.CharField(blank=True, default='', max_length=20),
            preserve_default=False,
        ),
    ]
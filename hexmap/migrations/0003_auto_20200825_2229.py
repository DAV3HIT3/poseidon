# Generated by Django 3.1 on 2020-08-25 22:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hexmap', '0002_auto_20200814_2023'),
    ]

    operations = [
        migrations.AlterField(
            model_name='region',
            name='name',
            field=models.CharField(max_length=120),
        ),
    ]

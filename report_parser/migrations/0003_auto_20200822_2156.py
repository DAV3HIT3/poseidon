# Generated by Django 3.1 on 2020-08-22 21:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('report_parser', '0002_userreport_json_data'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userreport',
            name='json_data',
            field=models.JSONField(default=dict),
        ),
    ]
# Generated by Django 3.1 on 2020-08-24 23:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('atlantis', '0016_auto_20200824_2330'),
    ]

    operations = [
        migrations.AddField(
            model_name='turnevent',
            name='event_msg',
            field=models.CharField(blank=True, max_length=120),
        ),
        migrations.AddField(
            model_name='turnevent',
            name='unit',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='atlantis.unit'),
        ),
    ]
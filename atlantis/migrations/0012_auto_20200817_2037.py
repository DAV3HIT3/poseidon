# Generated by Django 3.1 on 2020-08-17 20:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('atlantis', '0011_auto_20200817_1811'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userorder',
            name='turn',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='atlantis.userturn'),
        ),
    ]

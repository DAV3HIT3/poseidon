# Generated by Django 3.1 on 2020-08-25 23:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Point',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('x', models.IntegerField()),
                ('y', models.IntegerField()),
                ('z', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='RegionType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Region',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120)),
                ('coordinate', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hexmap.point')),
                ('region_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hexmap.regiontype')),
            ],
        ),
    ]

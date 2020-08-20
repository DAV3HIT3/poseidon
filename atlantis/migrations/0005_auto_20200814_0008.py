# Generated by Django 3.1 on 2020-08-14 00:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('atlantis', '0004_auto_20200813_2338'),
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('description', models.CharField(max_length=120)),
                ('required_skill', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='atlantis.skilllevel')),
            ],
        ),
        migrations.CreateModel(
            name='UnitDetail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120)),
                ('description', models.CharField(max_length=120)),
                ('is_mage', models.BooleanField(default=False)),
                ('is_quartermaster', models.BooleanField(default=False)),
                ('faction', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='atlantis.faction')),
                ('user_turn', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='atlantis.userturn')),
            ],
        ),
        migrations.RemoveField(
            model_name='raceskill',
            name='max_level',
        ),
        migrations.RemoveField(
            model_name='raceskill',
            name='skill',
        ),
        migrations.RemoveField(
            model_name='unit',
            name='description',
        ),
        migrations.RemoveField(
            model_name='unit',
            name='faction',
        ),
        migrations.RemoveField(
            model_name='unit',
            name='is_mage',
        ),
        migrations.RemoveField(
            model_name='unit',
            name='is_quartermaster',
        ),
        migrations.RemoveField(
            model_name='unit',
            name='maintenance_cost',
        ),
        migrations.RemoveField(
            model_name='unit',
            name='name',
        ),
        migrations.RemoveField(
            model_name='unit',
            name='purchase_cost',
        ),
        migrations.RemoveField(
            model_name='unit',
            name='user_turn',
        ),
        migrations.AddField(
            model_name='raceskill',
            name='race',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='atlantis.race'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='raceskill',
            name='skill_level',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='atlantis.skilllevel'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='unitmember',
            name='maintenance_cost',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='unitmember',
            name='purchase_cost',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.CreateModel(
            name='UnitItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='atlantis.item')),
                ('unit', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='atlantis.unitdetail')),
            ],
        ),
        migrations.AlterField(
            model_name='unitflag',
            name='unit',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='atlantis.unitdetail'),
        ),
        migrations.AlterField(
            model_name='unitmember',
            name='unit',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='atlantis.unitdetail'),
        ),
        migrations.AlterField(
            model_name='unitskill',
            name='unit',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='atlantis.unitdetail'),
        ),
    ]
# Generated by Django 3.1 on 2020-08-14 20:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('atlantis', '0005_auto_20200814_0008'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='item',
            name='required_skill',
        ),
        migrations.RemoveField(
            model_name='unitdetail',
            name='user_turn',
        ),
        migrations.AddField(
            model_name='item',
            name='capacity',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='item',
            name='purchase_cost',
            field=models.IntegerField(default=0, help_text='Withdraw cost'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='item',
            name='weight',
            field=models.IntegerField(default=1),
        ),
        migrations.AddField(
            model_name='unitdetail',
            name='silver',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='unitdetail',
            name='turn',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='atlantis.turn'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='unititem',
            name='quantity',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.CreateModel(
            name='ProductionSkill',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('production_time', models.IntegerField()),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='atlantis.item')),
                ('required_skill', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='atlantis.skilllevel')),
            ],
        ),
        migrations.CreateModel(
            name='ProductionMaterial',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField()),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='atlantis.item')),
                ('production_skill', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='atlantis.productionskill')),
            ],
        ),
    ]

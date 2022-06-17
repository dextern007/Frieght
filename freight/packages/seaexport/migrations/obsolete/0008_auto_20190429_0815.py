# Generated by Django 2.1.3 on 2019-04-29 08:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('freightman', '0005_auto_20190425_1225'),
        ('seaexport', '0007_auto_20190429_0744'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='seaexportcontainerconsolshipment',
            name='feeder_arrival_port',
        ),
        migrations.RemoveField(
            model_name='seaexportcontainerconsolshipment',
            name='feeder_departure_port',
        ),
        migrations.RemoveField(
            model_name='seaexportcontainerconsolshipment',
            name='mother_arrival_port',
        ),
        migrations.RemoveField(
            model_name='seaexportcontainerconsolshipment',
            name='mother_departure_port',
        ),
        migrations.AddField(
            model_name='seaexportcontainerconsolshipment',
            name='feeder_arrival_city',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='feeder_arrival_port', to='freightman.City'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='seaexportcontainerconsolshipment',
            name='feeder_departure_city',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='feeder_dept_port', to='freightman.City'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='seaexportcontainerconsolshipment',
            name='mother_arrival_city',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='mother_arrival_port', to='freightman.City'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='seaexportcontainerconsolshipment',
            name='mother_departure_city',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='mother_dept_port', to='freightman.City'),
            preserve_default=False,
        ),
    ]
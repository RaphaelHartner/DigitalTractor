# Generated by Django 3.2.3 on 2021-06-07 15:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_alter_sensorimplementation_sensor_model'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='dataacquisitionmodule',
            name='sensors',
        ),
        migrations.AlterField(
            model_name='dataacquisitionmodule',
            name='dam_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='dams', to='main.dataacquisitionmoduletype'),
        ),
        migrations.AlterField(
            model_name='measuredvariable',
            name='sensor_model',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='measured_variables', to='main.sensormodel'),
        ),
        migrations.AlterField(
            model_name='pinusage',
            name='sensor_implementation',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='pin_usages', to='main.sensorimplementation'),
        ),
        migrations.AlterField(
            model_name='requiredpin',
            name='communication_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='required_pins', to='main.communicationtype'),
        ),
        migrations.AlterField(
            model_name='sensorimplementation',
            name='component',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sensor_implementations', to='main.component'),
        ),
        migrations.AlterField(
            model_name='sensorimplementation',
            name='dam',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sensor_implementations', to='main.dataacquisitionmodule'),
        ),
        migrations.AlterField(
            model_name='sensorimplementation',
            name='sensor_model',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='sensor_implementations', to='main.sensormodel'),
        ),
        migrations.AlterField(
            model_name='sensormodel',
            name='communication_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sensor_models', to='main.communicationtype'),
        ),
        migrations.AlterField(
            model_name='sensormodel',
            name='sensor_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sensor_models', to='main.sensortype'),
        ),
    ]

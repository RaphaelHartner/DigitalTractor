# Generated by Django 3.2.3 on 2021-06-07 11:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_alter_pinusage_required_pin'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sensorimplementation',
            name='sensor_model',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='main.sensormodel'),
        ),
    ]
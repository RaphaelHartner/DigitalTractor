from django.db import models

# Create your models here.
class SensorType(models.Model):
    name = models.CharField(max_length=80)

class CommunicationType(models.Model):
    communication_name = models.CharField(max_length=80)

class RequiredPin(models.Model):
    communication_type = models.ForeignKey(CommunicationType, on_delete=models.CASCADE)
    pin_name = models.CharField(max_length=80)

class SensorModel(models.Model):
    sensor_type = models.ForeignKey(SensorType, on_delete=models.CASCADE)
    communication_type = models.ForeignKey(CommunicationType, on_delete=models.CASCADE)
    model_name = models.CharField(max_length=80)

class MeasuredVariable(models.Model):
    sensor_model = models.ForeignKey(SensorModel, on_delete=models.CASCADE)
    variable_name = models.CharField(max_length=80)
    unit = models.CharField(max_length=80)

# Data Acquisition Module
class DataAcquisitionModuleType(models.Model):
    dam_name = models.CharField(max_length=80)

class DataAcquisitionModule(models.Model):
    dam_type = models.ForeignKey(DataAcquisitionModuleType, on_delete=models.CASCADE)
    installation_date = models.DateTimeField()
    sensors = models.ManyToManyField(
        SensorModel,
        through='SensorImplementation',
        through_fields=('dam', 'sensor_model'))

class Component(models.Model):
    component_name = models.CharField(max_length=80)
    parent_component = models.ForeignKey('Component', null=True, on_delete=models.SET_NULL)

class SensorImplementation(models.Model):
    dam = models.ForeignKey(DataAcquisitionModule, on_delete=models.CASCADE)
    sensor_model = models.ForeignKey(SensorModel, on_delete=models.CASCADE)
    component = models.ForeignKey(Component, on_delete=models.CASCADE)


class PinUsage(models.Model):
    sensor_implementation=models.ForeignKey(SensorImplementation, on_delete=models.CASCADE)
    required_pin = models.ForeignKey(RequiredPin, on_delete=models.CASCADE)
    assigned_pin = models.CharField(max_length=20)

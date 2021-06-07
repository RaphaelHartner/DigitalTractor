from django.db import models

# Create your models here.
class SensorType(models.Model):
    name = models.CharField(max_length=80)
    def __str__(self):
        return self.name

class CommunicationType(models.Model):
    communication_name = models.CharField(max_length=80)
    def __str__(self):
        return self.communication_name

class RequiredPin(models.Model):
    communication_type = models.ForeignKey(CommunicationType, on_delete=models.CASCADE, related_name='required_pins')
    pin_name = models.CharField(max_length=80)
    def __str__(self):
        return self.communication_type.communication_name + "_" + self.pin_name

class SensorModel(models.Model):
    sensor_type = models.ForeignKey(SensorType, on_delete=models.CASCADE, related_name='sensor_models')
    communication_type = models.ForeignKey(CommunicationType, on_delete=models.CASCADE, related_name='sensor_models')
    model_name = models.CharField(max_length=80)
    def __str__(self):
        return self.sensor_type.name + "_" + self.model_name

class MeasuredVariable(models.Model):
    sensor_model = models.ForeignKey(SensorModel, on_delete=models.CASCADE, related_name='measured_variables')
    variable_name = models.CharField(max_length=80)
    unit = models.CharField(max_length=80)
    def __str__(self):
        return self.sensor_model.model_name + "_" + self.variable_name

# Data Acquisition Module
class DataAcquisitionModuleType(models.Model):
    dam_name = models.CharField(max_length=80)
    def __str__(self):
        return self.dam_name

class DataAcquisitionModule(models.Model):
    dam_type = models.ForeignKey(DataAcquisitionModuleType, on_delete=models.CASCADE, related_name='dams')
    installation_date = models.DateTimeField()
    #sensors = models.ManyToManyField(
    #    SensorModel,
    #    through='SensorImplementation',
    #    through_fields=('dam', 'sensor_model'))

    def __str__(self):
        return self.dam_type.dam_name

class Component(models.Model):
    component_name = models.CharField(max_length=80)
    parent_component = models.ForeignKey('self', on_delete=models.SET_NULL, null=True, default=None, blank=True)
    def __str__(self):
        return self.component_name

class SensorImplementation(models.Model):
    dam = models.ForeignKey(DataAcquisitionModule, on_delete=models.CASCADE, related_name='sensor_implementations')
    sensor_model = models.OneToOneField(SensorModel, on_delete=models.CASCADE, related_name='sensor_implementations')
    component = models.ForeignKey(Component, on_delete=models.CASCADE, related_name='sensor_implementations')
    def __str__(self):
        return str(self.sensor_model) + " at " + str(self.dam) + " measuring " + str(self.component)

class PinUsage(models.Model):
    sensor_implementation=models.ForeignKey(SensorImplementation, on_delete=models.CASCADE, related_name='pin_usages')
    required_pin = models.OneToOneField(RequiredPin, on_delete=models.CASCADE)
    assigned_pin = models.CharField(max_length=20)
    def __str__(self):
        return str(self.sensor_implementation) + " (" + str(self.required_pin.pin_name) + " on " + str(self.assigned_pin) + ")"

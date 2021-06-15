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
    def get_full_name(self):
        if self.parent_component:
            return self.parent_component.get_full_name() + '/' + self.component_name
        else:
            return self.component_name

    def __str__(self):
        return self.component_name

class SensorImplementation(models.Model):
    dam = models.ForeignKey(DataAcquisitionModule, on_delete=models.CASCADE, related_name='sensor_implementations')
    sensor_model = models.OneToOneField(SensorModel, on_delete=models.CASCADE, related_name='sensor_implementations')
    component = models.ForeignKey(Component, on_delete=models.CASCADE, related_name='sensor_implementations')
    cycle_time = models.IntegerField(default=1000) # cycle time in milliseconds
    measured_variable = models.CharField(max_length=80,blank=True, default='')
    measured_unit = models.CharField(max_length=80, blank=True, default='')
    def __str__(self):
        return str(self.sensor_model) + " at " + str(self.dam) + " measuring " + str(self.component)

class PinUsage(models.Model):
    sensor_implementation=models.ForeignKey(SensorImplementation, on_delete=models.CASCADE, related_name='pin_usages')
    required_pin = models.OneToOneField(RequiredPin, on_delete=models.CASCADE)
    assigned_pin = models.CharField(max_length=20)
    def __str__(self):
        return str(self.sensor_implementation) + " (" + str(self.required_pin.pin_name) + " on " + str(self.assigned_pin) + ")"


######################### model views #######################################
class PinUsageDataView():
    def __init__(self, required_pin):
        self.pin_name = required_pin.pin_name
        self.pin_number = required_pin.pinusage.assigned_pin

class SensorImplDataView():
    def __init__(self, sensor_impl:SensorImplementation):
        self.component_name = sensor_impl.component.get_full_name()
        self.cycle_time = sensor_impl.cycle_time
        self.measured_variable = sensor_impl.measured_variable
        self.measured_unit = sensor_impl.measured_unit
        self.sensor_name = sensor_impl.sensor_model.model_name
        self.communication_name = sensor_impl.sensor_model.communication_type.communication_name
        self.pins = []
        for p in sensor_impl.sensor_model.communication_type.required_pins.all():
            self.pins.append(PinUsageDataView(p))


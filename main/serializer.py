import main.models as models
from rest_framework import serializers

class SensorTypeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.SensorType
        fields = ['url','name', 'sensor_models']

class SensorModelSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.SensorModel
        fields = ['url','model_name','sensor_type', 'communication_type', 'measured_variables', 'sensor_implementations']

class CommunicationTypeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.CommunicationType
        fields = ['url', 'communication_name', 'sensor_models', 'required_pins']

class RequiredPinSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.RequiredPin
        fields = '__all__'

class DAMTypeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.DataAcquisitionModuleType
        fields = ['url', 'dam_name', 'dams']

class DAMSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.DataAcquisitionModule
        fields = ['url', 'dam_type', 'sensor_implementations']

class ComponentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Component
        fields = ['url', 'component_name', 'parent_component', 'sensor_implementations']

class SensorImplementationSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.SensorImplementation
        depth=3
        #fields = ['url', 'dam', 'sensor_model', 'component', 'pin_usages', 'measured_variable', 'measured_unit','cycle_time']
        fields= '__all__'

class PinUsageSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.PinUsage
        fields = '__all__'


######################### model views serializer #######################################

class PinUsageDataSerializer(serializers.Serializer):
    pin_name = serializers.CharField(max_length=80)
    pin_number = serializers.CharField(max_length=20)

class SensorImplDataSerializer(serializers.Serializer):
    component_name = serializers.CharField(max_length=80)
    cycle_time = serializers.IntegerField()
    measured_variable = serializers.CharField(max_length=80)
    measured_unit = serializers.CharField(max_length=80)
    sensor_name = serializers.CharField(max_length=80)
    communication_name = serializers.CharField(max_length=80)
    pins = PinUsageDataSerializer(many=True)





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


class MeasuredVariableSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.MeasuredVariable
        fields = '__all__'

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
        fields = ['url', 'dam', 'sensor_model', 'component', 'pin_usages']

class PinUsageSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.PinUsage
        fields = '__all__'


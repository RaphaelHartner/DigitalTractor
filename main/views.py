from django.shortcuts import render
from django.http import HttpResponse
import main.models as models
import main.serializer as ser
from rest_framework import viewsets
 
# Create your views here.

def index(request):
	return HttpResponse('Hello tractor!')

class SensorTypeViewSet(viewsets.ModelViewSet):
    queryset = models.SensorType.objects.all()
    serializer_class = ser.SensorTypeSerializer

class SensorModelViewSet(viewsets.ModelViewSet):
    queryset = models.SensorModel.objects.all()
    serializer_class = ser.SensorModelSerializer

class MeasuredVariableViewSet(viewsets.ModelViewSet):
    queryset = models.MeasuredVariable.objects.all()
    serializer_class = ser.MeasuredVariableSerializer

class CommunicationTypeViewSet(viewsets.ModelViewSet):
    queryset = models.CommunicationType.objects.all()
    serializer_class = ser.CommunicationTypeSerializer

class RequiredPinViewSet(viewsets.ModelViewSet):
    queryset = models.RequiredPin.objects.all()
    serializer_class = ser.RequiredPinSerializer

class DAMTypeViewSet(viewsets.ModelViewSet):
    queryset = models.DataAcquisitionModuleType.objects.all()
    serializer_class = ser.DAMTypeSerializer

class DAMViewSet(viewsets.ModelViewSet):
    queryset = models.DataAcquisitionModule.objects.all()
    serializer_class = ser.DAMSerializer

class ComponentViewSet(viewsets.ModelViewSet):
    queryset = models.Component.objects.all()
    serializer_class = ser.ComponentSerializer

class SensorImplementationViewSet(viewsets.ModelViewSet):
    queryset = models.SensorImplementation.objects.all()
    serializer_class = ser.SensorImplementationSerializer

class PinUsageViewSet(viewsets.ModelViewSet):
    queryset = models.PinUsage.objects.all()
    serializer_class = ser.PinUsageSerializer



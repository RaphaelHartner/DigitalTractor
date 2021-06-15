from django.shortcuts import render
from django.http import HttpResponse
import main.models as models
import main.serializer as ser

from rest_framework import viewsets
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response
from rest_framework.decorators import api_view
# Create your views here.

@api_view(['GET'])
def sensor_impl_data(request, dam_id):
    impl_list=[]
    for impl in  models.SensorImplementation.objects.filter(dam_id=dam_id):
        data_view = models.SensorImplDataView(impl)
        impl_ser = ser.SensorImplDataSerializer(data_view)
        impl_list.append(impl_ser.data)
    return Response(impl_list)


def index(request):
	return HttpResponse('Hello tractor!')

class SensorTypeViewSet(viewsets.ModelViewSet):
    queryset = models.SensorType.objects.all()
    serializer_class = ser.SensorTypeSerializer

class SensorModelViewSet(viewsets.ModelViewSet):
    queryset = models.SensorModel.objects.all()
    serializer_class = ser.SensorModelSerializer

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



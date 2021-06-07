from django.urls import path, include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'sensor_type', views.SensorTypeViewSet)
router.register(r'sensor_models', views.SensorModelViewSet)
router.register(r'measured_variable', views.MeasuredVariableViewSet)
router.register(r'communication_type', views.CommunicationTypeViewSet)
router.register(r'required_pin', views.RequiredPinViewSet)
router.register(r'dam_type', views.DAMTypeViewSet)
router.register(r'dam', views.DAMViewSet)
router.register(r'component', views.ComponentViewSet)
router.register(r'sensor_implementation', views.SensorImplementationViewSet)
router.register(r'pin_usage', views.PinUsageViewSet)



urlpatterns=[
	path('',views.index, name='index'),
    path('api/', include(router.urls))
]

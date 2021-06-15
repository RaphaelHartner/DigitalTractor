from django.contrib import admin

# Register your models here.
from .models import SensorType
from .models import SensorModel
from .models import CommunicationType
from .models import RequiredPin
from .models import DataAcquisitionModuleType
from .models import DataAcquisitionModule
from .models import Component
from .models import SensorImplementation
from .models import PinUsage

admin.site.register(SensorType)
admin.site.register(SensorModel)
admin.site.register(CommunicationType)
admin.site.register(RequiredPin)
admin.site.register(DataAcquisitionModuleType)
admin.site.register(DataAcquisitionModule)
admin.site.register(Component)
admin.site.register(SensorImplementation)
admin.site.register(PinUsage)


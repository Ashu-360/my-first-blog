from django.contrib import admin
from .models import Slot,Slip,VehicleInfo,Floor

admin.site.register(VehicleInfo)
admin.site.register(Slip)
admin.site.register(Floor)
admin.site.register(Slot)
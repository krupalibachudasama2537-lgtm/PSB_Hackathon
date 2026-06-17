from django.contrib import admin
from .models import Device, LoginHistory, SecurityAlert

admin.site.register(Device)
admin.site.register(LoginHistory)
admin.site.register(SecurityAlert)
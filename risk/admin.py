from django.contrib import admin
from .models import RiskScore, RiskEvent

admin.site.register(RiskScore)
admin.site.register(RiskEvent)
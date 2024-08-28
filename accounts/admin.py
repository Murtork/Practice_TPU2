from django.contrib import admin

from django.contrib import admin
from .models import Consumer, Tariff, ConsumptionRecord, ContractPhys, ContractLegal

admin.site.register(Consumer)
admin.site.register(Tariff)
admin.site.register(ConsumptionRecord)
admin.site.register(ContractPhys)
admin.site.register(ContractLegal)

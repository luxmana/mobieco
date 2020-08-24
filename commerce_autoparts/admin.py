from django.contrib import admin

from .models import *


# Register your models here.
admin.site.register(Logistic)
admin.site.register(OrderRequest)
admin.site.register(Status)
admin.site.register(Rank)
admin.site.register(Currency)
admin.site.register(RequestStatus)
admin.site.register(PurchaseUpdate)

from django.contrib import admin

from .models import *


# Register your models here.
admin.site.register(Logistic)
admin.site.register(OrderRequest)
admin.site.register(Status)


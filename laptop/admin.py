from django.contrib import admin

from laptop.models import Laptop, Brand, Gadget

admin.site.register(Laptop)
admin.site.register(Brand)
admin.site.register(Gadget)

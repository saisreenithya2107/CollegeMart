from django.contrib import admin
from .models import Orders_Buying, Orders_Leasing, Notification
# Register your models here.
admin.site.register(Orders_Buying)
admin.site.register(Orders_Leasing)
admin.site.register(Notification)
from django.contrib import admin
from .models import Equipment, Customer, Order, Lake, Beach, Schedule
from smart_selects.db_fields import ChainedForeignKey

@admin.register(Equipment)
class EquipmentAdmin(admin.ModelAdmin):
    pass


@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    pass


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    pass


@admin.register(Lake)
class LakeAdmin(admin.ModelAdmin):

    pass


@admin.register(Beach)
class BeachAdmin(admin.ModelAdmin):
    pass


@admin.register(Schedule)
class ScheduleAdmin(admin.ModelAdmin):
    pass

admin.site.site_header = 'SUNRISE management'
admin.site.site_title = 'SUNRISE admin'
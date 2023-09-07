from django.contrib import admin

from gems.models import Customer, Deal, DealPacket, Gem


class CustomerAdmin(admin.ModelAdmin):
    list_display = (
        'pk',
        'user',
    )
    list_select_related = ('user',)
    empty_value_display = '--empty--'


class DealAdmin(admin.ModelAdmin):
    list_display = (
        'pk',
        'deal_packet',
        'customer',
        'gem',
        'total',
        'quantity',
        'date',
    )
    list_select_related = (
        'deal_packet',
        'customer',
        'customer__user',
        'gem',
    )
    empty_value_display = '--empty--'
    list_filter = ('deal_packet',)


class DealPacketAdmin(admin.ModelAdmin):
    list_display = (
        'pk',
        'created_at',
    )
    empty_value_display = '--empty--'


class GemAdmin(admin.ModelAdmin):
    list_display = (
        'pk',
        'name',
    )
    empty_value_display = '--empty--'


admin.site.register(Customer, CustomerAdmin)
admin.site.register(Deal, DealAdmin)
admin.site.register(DealPacket, DealPacketAdmin)
admin.site.register(Gem, GemAdmin)

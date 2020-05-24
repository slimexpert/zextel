from django.contrib import admin
# Register your models here.
from .models import slider, contact_support, postal, zone, Rate

class SliderAdmin(admin.ModelAdmin):
	list_display = ('sl_title', 'sl_number', 'sl_show',)

class Contact_supportAdmin(admin.ModelAdmin):
	list_display = ('supp_date', 'supp_name', 'supp_email', 'supp_tel', 'supp_cat',)

class ZoneAdmin(admin.ModelAdmin):
	list_display = ('zone_title', 'zone_number', 'zone_text', 'zone_show',)

class PostalAdmin(admin.ModelAdmin):
	list_display = ('postal_code', 'postal_title', 'postal_show', 'postal_zone',)

class RateAdmin(admin.ModelAdmin):
	list_display = ('rate_title', 'rate_title_text', 'rate_zone', 'rate_group', 'rate_number', 'rate_popular', 'rate_type', 'rate_speed', 'rate_summ', 'rate_tv_count' )
	list_filter = ('rate_zone', 'rate_type')

admin.site.register(slider, SliderAdmin)
admin.site.register(contact_support, Contact_supportAdmin)
admin.site.register(zone, ZoneAdmin)
admin.site.register(postal, PostalAdmin)
admin.site.register(Rate, RateAdmin)

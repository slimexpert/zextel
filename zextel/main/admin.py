from django.contrib import admin
# Register your models here.
from .models import slider, contact_support

class SliderAdmin(admin.ModelAdmin):
	list_display = ('sl_title', 'sl_number', 'sl_show',)

class Contact_supportAdmin(admin.ModelAdmin):
	list_display = ('supp_date', 'supp_name', 'supp_email', 'supp_tel', 'supp_cat',)

admin.site.register(slider, SliderAdmin)
admin.site.register(contact_support, Contact_supportAdmin)


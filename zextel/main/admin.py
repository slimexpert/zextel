from django.contrib import admin
# Register your models here.
from .models import slider

class SliderAdmin(admin.ModelAdmin):
	list_display = ('sl_title', 'sl_number', 'sl_show',)

admin.site.register(slider, SliderAdmin)
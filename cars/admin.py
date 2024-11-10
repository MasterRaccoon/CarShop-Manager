from django.contrib import admin
from cars.models import Car, Brand

class BrandAdmin(admin.ModelAdmin):
	list_display = ('name',)
	search_fields = ('name',)

class CarAdmin(admin.ModelAdmin):
	list_display = ('model', 'brand', 'factory_year', 'model_year', 'plate', 'value', 'photo')
	search_fields = ('model', 'brand__name', 'plate',)

admin.site.register(Brand, BrandAdmin)
admin.site.register(Car, CarAdmin)

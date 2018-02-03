from django.contrib import admin
from metalconstr.models import Category, Construction

class CategoryAdmin(admin.ModelAdmin):
	fieldsets = [
		(None,										{'fields':['cat_name']}),
		('Category description',					{'fields':['cat_description']}),
	]

	list_display = 	('cat_name', 'id')
	search_fields = ['cat_name']

class ConstructionAdmin(admin.ModelAdmin):
	fieldsets = [
		(None, 					 				{'fields': ['category']}),
		('Construction name',					{'fields': ['const_name']}),
		('Construction description',			{'fields': ['const_description']}),
		('Construction image',					{'fields': ['const_imagename']}),
	]

	list_display = 	('const_name','category', 'id')
	list_filter = 	['category']
	search_fields = ['category']

admin.site.register(Category, CategoryAdmin)
admin.site.register(Construction, ConstructionAdmin)


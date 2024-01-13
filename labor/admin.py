from django.contrib import admin
from .models import *

# Register your models here.

@admin.register(labor_register)
class labor_register_admin(admin.ModelAdmin):
    list_display = ['labor_id', 'first_name', 'last_name', 'email', 'mobile']
    list_display_links = ['labor_id', 'email']
    list_editable = ['first_name', 'last_name','mobile']
    search_fields = ['labor_id', 'first_name', 'last_name', 'email', 'mobile']
    list_filter = ['first_name']
    list_per_page = 2
from django.contrib import admin
from .models import *
# Register your models here.
admin.site.site_header = 'Work-Diary'
admin.site.index_title = 'Work Diary Dashboard'
admin.site.site_title = 'WORK-DIARY'

admin.site.register(counter_table)

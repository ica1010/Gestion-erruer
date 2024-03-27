from django.contrib import admin
from . models import *
# Register your models here.


class Table1Admin(admin.ModelAdmin):
    list_display = ['field1','field2','field3','field4','field5']

class Table2Admin(admin.ModelAdmin):
    list_display = ['field1','field2','field3','field4','field5']

class Table3Admin(admin.ModelAdmin):
    list_display = ['field1','field2','field3','field4','field5']
admin.site.register(Table1,Table1Admin)
admin.site.register(Table2,Table2Admin)
admin.site.register(Table3, Table3Admin)
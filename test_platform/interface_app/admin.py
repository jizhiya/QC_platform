from django.contrib import admin
from interface_app.models import TestCase,TestTask

# Register your models here.
#映射到admin后台管理系统
class TestCaseAdmin(admin.ModelAdmin):
    list_display = ['module','name','url','req_method','req_method','req_type','req_header','req_parameter','responses_assert']

class TestTaskAdmin(admin.ModelAdmin):
    list_display = ['name','describe','cases',"status"]



admin.site.register(TestCase,TestCaseAdmin)
admin.site.register(TestTask,TestTaskAdmin)

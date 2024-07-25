from django.contrib import admin
from .models import *


# Register your models here.


@admin.register(AboutUs)
class AboutUsAdmin(admin.ModelAdmin):
    list_display = ['history',
                    'why_us',]

@admin.register(Employees)
class EmployeesAdmin(admin.ModelAdmin):
    list_display = ['image',
                    'employees_name',
                    'position']
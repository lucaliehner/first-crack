from django.contrib import admin
from .models import Event, Employee
from import_export.admin import ImportExportModelAdmin

@admin.register(Event)
class EventAdmin(ImportExportModelAdmin):
    pass


@admin.register(Employee)
class EmployeeAdmin(ImportExportModelAdmin):
    pass

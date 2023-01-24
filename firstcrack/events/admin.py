from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from .models import Event
# Register your models here.
admin.site.register(Event)

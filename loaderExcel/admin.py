from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from .models import Student

# Register your models here.

@admin.register(Student)
class StudentAdmin(ImportExportModelAdmin):
    list_display = ("name", "lastName", "email", "phone", "course", "teacher", "score")

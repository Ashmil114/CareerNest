from django.contrib import admin
from .models import StudentModel


class StudentAdmin(admin.ModelAdmin):
    list_display = ("user","department")

admin.site.register(StudentModel,StudentAdmin)

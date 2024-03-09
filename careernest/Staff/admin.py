from django.contrib import admin
from .models import JobsModel,ApplyedJobModel

# Register your models here.
class ApplyedJobAdmin(admin.ModelAdmin):
    list_display = ("job", "user", "status")

admin.site.register(JobsModel)
admin.site.register(ApplyedJobModel, ApplyedJobAdmin)

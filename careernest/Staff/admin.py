from django.contrib import admin
from .models import JobsModel,ApplyedJobModel,CompanyModel,SaveJobModel

# Register your models here.
class ApplyedJobAdmin(admin.ModelAdmin):
    list_display = ("job", "user", "status")

class SaveJobAdmin(admin.ModelAdmin):
    list_display = ("job", "user")

class JobAdmin(admin.ModelAdmin):
    list_display = ("title","company","type","vaccancies","package","experiance")

admin.site.register(CompanyModel)
admin.site.register(JobsModel,JobAdmin)
admin.site.register(SaveJobModel,SaveJobAdmin)
admin.site.register(ApplyedJobModel, ApplyedJobAdmin)

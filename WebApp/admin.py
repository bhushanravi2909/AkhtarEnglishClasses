from django.contrib import admin
from WebApp.models import std_reg,BatchTiming,Assignment,notification

# Register your models here.

class stdAdmin(admin.ModelAdmin):
    list_display=['Name','Father_Name','Mother_Name','Email','Confirm_Email','Mobile','Address','ZipCode']
admin.site.register(std_reg,stdAdmin)

class BatchTimingAdmin(admin.ModelAdmin):
    list_display=['Batch','Timing']
admin.site.register(BatchTiming,BatchTimingAdmin)


class AssignmentAdmin(admin.ModelAdmin):
    list_display=['Class','Title','Posted_date','Submission_Date']
admin.site.register(Assignment,AssignmentAdmin)

class notificationAdmin(admin.ModelAdmin):
    list_display=['Subject','Posted_date']
admin.site.register(notification,notificationAdmin)

from django.contrib import admin
from .models import *

# Register your models here.
@admin.register(Staff)
class StaffAdmin(admin.ModelAdmin):
    list_display = ['fullname', 'phone', 'dept', 'dob', 'get_role', 'status']
    search_fields = ['user__first_name', 'user__last_name', 'phone', 'dept']
    list_filter = ['status', 'dept']
    readonly_fields = ['dob']
    def fullname(self, obj):
        if obj.user and obj.user.first_name:
            return f'{obj.user.first_name} {obj.user.last_name}'
        return "N/A"
    fullname.short_description = 'Full Name'

    def get_role(self,obj):
        if obj.supervisor:
            return 'Supervisor'
        return "N/A"
    get_role.short_description = 'Role'

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ['title','status','persons_assigned','priority','due_date','created_date']
    search_fields = ['title', 'status', 'assigned_to__user__first_name', 'assigned_to__user__last_name', 'priority']

    def persons_assigned(self, obj):
        if obj.assigned_to.all():
            return  obj.assigned_to.count()
        return 0
    persons_assigned.short_description = 'Assigned To'

@admin.register(SanitizationReport)
class SanitizationReportAdmin(admin.ModelAdmin):
    list_display = ['title', 'reporter' ,'category','created_date']
    search_fields = ['title', 'category', 'created_date']

    list_filter = [ 'category']
    readonly_fields = ['created_date']

    def reporter(self, obj):
        if obj.reporter_user:
            return f'{obj.reporter_user.first_name} {obj.reporter_user.last_name}'
        return 'N/A'

    reporter.short_description = 'Reporter'

admin.site.register(Activity)
admin.site.register(Notification)
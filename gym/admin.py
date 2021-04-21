from django.contrib import admin
from .models import Plan, Enquiry, Equipment, Member, Attendance, AttendanceReport

# Register your models here.

admin.site.register(Plan)
admin.site.register(Enquiry)
admin.site.register(Equipment)
admin.site.register(Member)
admin.site.register(Attendance)
admin.site.register(AttendanceReport)

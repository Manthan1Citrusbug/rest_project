from django.contrib import admin
from app_ser_insert.models import Student
# Register your models here.

class StudentAdmin(admin.ModelAdmin):
    list_display = ['id','name','roll','city']
admin.site.register(Student, StudentAdmin)
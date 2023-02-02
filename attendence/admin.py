from django.contrib import admin
from . import models

@admin.register(models.Profile)
class ProfileAdmin(admin.ModelAdmin):
	pass

@admin.register(models.Faculty)
class FacultyAdmin(admin.ModelAdmin):
	pass

@admin.register(models.Department)
class DepartmentAdmin(admin.ModelAdmin):
	pass

@admin.register(models.Program)
class ProgramAdmin(admin.ModelAdmin):
	pass

@admin.register(models.Course)
class CourseAdmin(admin.ModelAdmin):
	pass

@admin.register(models.Attendence)
class AttendenceAdmin(admin.ModelAdmin):
	pass
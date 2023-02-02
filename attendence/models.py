from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	roll = models.CharField(max_length=10, null=True, blank=True)
	faculty = models.ForeignKey('Faculty', on_delete=models.CASCADE)
	department = models.ForeignKey('Department', on_delete=models.CASCADE)
	program = models.ForeignKey('Program', on_delete=models.CASCADE)
	courses = models.ManyToManyField('Course')


class Faculty(models.Model):
	name = models.CharField(max_length=250)

	def __str__(self):
		return self.name

class Department(models.Model):
	name = models.CharField(max_length=250)

	def __str__(self):
		return self.name

class Program(models.Model):
	name = models.CharField(max_length=250)

	def __str__(self):
		return self.name

class Course(models.Model):
	name = models.CharField(max_length=250)
	course_code = models.CharField(max_length=10)
	def __str__(self):
		return self.name

class Attendence(models.Model):
	std = models.ForeignKey(User, on_delete=models.CASCADE)
	course = models.ForeignKey(Course, on_delete=models.CASCADE)
	is_present = models.BooleanField()
	date = models.DateField(auto_now_add=True)

	def __str__(self):
		return self.std.username
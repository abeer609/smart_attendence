from django.shortcuts import render
from django.http import JsonResponse, HttpResponseRedirect
from .utils import create_token, check_token
from rest_framework.response import Response
# from rest_framework.views import APIView
from .models import Attendence, Profile, Course
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required, permission_required
import datetime
from django.forms import forms

@login_required(login_url='/login/')
@permission_required("attendence.view_attendence", raise_exception=True)
def index(request):
    courses = Course.objects.all()
    return render(request, "attendence/courses.html", {'courses': courses})

def scan(request):
    return render(request, "attendence/scan.html")

@login_required(login_url='/login/')
@permission_required("attendence.view_attendence", raise_exception=True)
def token(request, course_code):
    token = create_token({"course":course_code}, exp=10)
    return render(request, 'attendence/index.html', {'token': token})

def verify_token(request, token):
    success, course = check_token(token)
    if success:
        user = request.user
        course = Course.objects.get(course_code=course)
        attendence, created = Attendence.objects.update_or_create(std=user, course=course, is_present=True, date=datetime.date.today())
        if created:
            return JsonResponse({"success":True, "course": course.course_code, "user":request.user.username})
        else:
            return JsonResponse({"success": True, "msg": f"You are already presented on {course.name}"})
    else:
        return JsonResponse({"success":success, "course": course, "user":request.user.username})


def user_login(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        message = {}
        if user is not None:
            login(request, user)
            if user.has_perm('attendence.view_attendence'):
                return HttpResponseRedirect('/')
            else:
                return HttpResponseRedirect('/scan/')
        else:
            message['message']="Wrong username or password"
            return render(request, 'attendence/login.html', message)
    return render(request, 'attendence/login.html')

def user_logout(request):
    logout(request)
    return HttpResponseRedirect("/login")

def attendence_report(request, course_code):
    today_min = datetime.datetime.combine(datetime.date.today(), datetime.time.min)
    today_max = datetime.datetime.combine(datetime.date.today(), datetime.time.max)
    attendences = Attendence.objects.filter(course__course_code=course_code, date__range=(today_min, today_max))
    return render(request, 'attendence/report.html', {"attendences": attendences})
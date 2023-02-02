from django.urls import path
from .views import token, verify_token, index, scan, user_login, user_logout, attendence_report

urlpatterns = [
    path('', index),
    path('login/', user_login, name='login'),
    path('logout/', user_logout, name='login'),
    path('report/<str:course_code>/', attendence_report),
    path('scan/', scan),
    path('token/<str:course_code>/', token, name='course_token'),
    path('token/verify/<str:token>/', verify_token, name="verify_token"),
]
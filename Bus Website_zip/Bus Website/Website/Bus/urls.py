from django.contrib import admin
from django.urls import path
from Bus import views

urlpatterns = [
    path('', views.index, name='home'),
    path('signup/', views.signup, name='signup'),
    path('contact/', views.COntact, name='contact'),
    path('about/', views.about, name='about'),
    path('login/', views.admin_login, name='Admin_login'),
    path('logout/', views.admin_logout, name='Admin_logout'),
    path('viewpage/', views.admin_viewpage, name='Admin_viewpage'),
    path('students/', views.students, name='Admin_StudentsList'),
    path('success/',views.success,name="Success"),
    path('query/',views.query,name="Queries"),
    path('success/',views.query_success,name="Q_Success"),
    path('stupdates/',views.studentupdate,name="Student Updates"),
    path('aupdates/',views.adminupdate,name="Admin Updates"),
    path('s_signup/',views.studsignup,name="Student Signup")
]

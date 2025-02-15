from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="home")
    # path("blog/", views.blog, name="blog"),
    # path("about/", views.about, name="about"),
    # path("contact/", views.contact, name="contact"),
    # path("single/", views.single, name="single"),
    # path("course/", views.course, name="course"),
    # path("teacher/", views.teacher, name="teacher"),
    # path('signup/', views.signup, name='signup'),
    # # path('newlogin/', views.newlogin, name='newlogin'),
    # # path('basic/', views.basic, name='basic'),
    # path('dashboard/', views.dashboard, name='dashboard')
]
"""
URL configuration for Blog project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from Blog_page import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/',views.userlogin ,name='login'),
    path('register/',views.register ,name="register"),
    path('',views.homepage ,name="home"),
    path('home2/',views.homepage2 ,name="home2"),
    path('about/',views.about ,name="about"),
    path('about2/',views.about2 ,name="about2"),
    path('contact/',views.contact ,name="contact"),
    path('contact2/',views.contact2 ,name="contact2"),
    path('dashboard/',views.dashboard ,name="dashboard"),
    path('addpost/', views.add_post, name='addpost'),
    path('updatepost/<int:post_id>/', views.update_post, name='update_post'),

    path('delete<int:id>/', views.delete_post, name='deletepost'),
    path('all_blogs/', views.all_blogs, name='all_blogs'),
]
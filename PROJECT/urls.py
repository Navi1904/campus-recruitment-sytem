"""
URL configuration for project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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


from CAMPUS import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('jnnce/',views.jnncepage ,name="jnnce"),
    path('campus/',views.signpage ,name="signin"),
    path('login/',views.loginpage ,name="login"),
    path('index/',views.homepage ,name="index"),
    path('logout/',views.logoutpage ,name="logout"),
    path('jobs/', views.job_list, name='job_list'),

    path('job/<int:job_id>/', views.job_detail, name='job_detail'),
    path('job/<int:job_id>/apply/', views.apply_for_job, name='apply_for_job'),
    


]
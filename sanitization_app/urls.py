"""
URL configuration for sanitization_app project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
from django.conf import settings
from django.conf.urls.static import static
from core.views import auth_views, user_views, staff_views, task_views

urlpatterns = [
    path("admin/", admin.site.urls),
    path('', auth_views.home, name='home'),
    path('sanititation/register/', auth_views.registerPage, name='register'),
    path('sanititation/login/', auth_views.loginPage, name='login'),
    path('sanititation/logout/', auth_views.logoutUser, name='logout'),
    path('sanititation/dashboard', staff_views.admin_Dashboard, name='admin_dashboard'),
    path('sanitation/user/', staff_views.userPage, name='user-page'),
    path('santitation/Task/', task_views.TaskList, name='Task'),

        #task create and delete
    path('create_task/', task_views.CreateTask, name='create_task'),
    path('update_task/<str:pk>', task_views.UpdateTask,name='update_task'),
    path('delete_task/<str:pk>/', task_views.deleteTask, name='delete_task'),
    
    #Staff
    path('staff/<str:pk_test>/', staff_views.staff, name='staff'),
    path('profile/', staff_views.profilesettings, name='profile'),

]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

"""crudoperation URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import path, include
from rest_framework.routers import DefaultRouter

from mixins import views
from modelviewset.views import StudentModelViewSet

router = DefaultRouter()

# router.register('studentapi', StudentViewSet, basename='student')
router.register('modelviewset_studentapi', StudentModelViewSet, basename='student')

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('user/', include('user.urls')),
    # path('modelviewset/', include('modelviewset.urls')),
    # path('mixins/', include('mixins.urls')),
    # path('', include(router.urls)),
    path('studentlistapi/', views.StudentList.as_view()),
    path('studentcreateapi/', views.StudentCreate.as_view()),
    path('studentretrieveapi/<int:pk>/', views.StudentRetrieve.as_view()),
    path('studentupdateapi/<int:pk>/', views.StudentUpdate.as_view()),
    path('studentdestroyapi/<int:pk>/', views.StudentDestroy.as_view()),
    path('studentLCapi/', views.StudentLC.as_view()),
    path('studentGUDapi/<int:pk>/', views.StudentGUD.as_view()),



    ]
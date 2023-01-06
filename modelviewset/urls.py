from django.urls import path

from . import views


urlpatterns = [

    path('viewset', views.StudentModelViewSet.as_view({'post': 'create', 'get': 'list', 'put': 'update',
                                                    'delete': 'destroy'}), name='cl'),

]
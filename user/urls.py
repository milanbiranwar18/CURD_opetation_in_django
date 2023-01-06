from django.urls import path

from . import views
from rest_framework.routers import DefaultRouter

from .views import StudentViewSet

# router = DefaultRouter()
# router.register('viewset', StudentViewSet.as_view, basename='student')
# urlpatterns= router.urls

# user_list = StudentViewSet.as_view({'get': 'list'})
# user_list1 = StudentViewSet.as_view({'get': 'create'})
# user_detail = StudentViewSet.as_view({'get': 'retrieve'})


urlpatterns = [
    path('create/', views.create, name='create'),
    path('update/', views.update, name='update'),
    path('get/', views.get, name='get'),
    path('delete/', views.delete, name='delete'),
    path('cl/', views.MyView.as_view(), name='cl'),
    path('subcl/', views.MyViewChild.as_view(), name='subcl'),
    path('viewset', views.StudentViewSet.as_view({'post': 'create', 'get': 'list', 'put': 'update',
                                                    'delete': 'destroy'}), name='cl'),

]
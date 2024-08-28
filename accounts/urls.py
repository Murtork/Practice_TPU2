from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('add/', views.add_consumption_record, name='add_consumption_record'),
    path('records/', views.consumption_records, name='consumption_records'),
    path('all-records/', views.all_consumption_records, name='all_consumption_records'),
    path('error/', views.error, name='error'),
]

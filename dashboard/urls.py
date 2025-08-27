from django.urls import path
from . import views

urlpatterns = [
   path('', views.home, name='home'),
   path('add_services/', views.add_services, name='add_services'),
   path('edit_service/<int:id>/', views.edit_service, name='edit_service'),
   path('delete_service/', views.delete_service, name='delete_service'),
   path('all_services/', views.all_services, name='all_services'),
   path('all_customers/', views.all_customers, name='all_customers'),
   path('all_appointment/', views.all_appointment, name='all_appointment'),
   path('logout/', views.logoutAdmin, name='logout'),
]
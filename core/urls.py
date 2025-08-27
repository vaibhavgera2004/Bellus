from django.urls import path
from . import views

urlpatterns = [
   path('', views.index, name='index'), 
   path('signup/', views.signup, name='signup'), 
   path('login/', views.login, name='login'),
   path('logout/', views.logout, name='logout'),
   path('services/', views.services, name='services'),
   path('delete-service/<int:id>/', views.delete_service, name='delete_service'), 
   path('contact/', views.contact, name='contact'),
   path('about/', views.about, name='about'),
   path('bookappointment/', views.bookappointment, name='bookappointment'),
   path('appointments/', views.appointments, name='appointments'),
   path('admin_login/', views.admin_login, name='admin_login'),
]
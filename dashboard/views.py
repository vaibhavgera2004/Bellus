from django.shortcuts import render, HttpResponse, redirect
from core.models import Customer, Service, Appointment
from .forms import AddServiceForm
from django.contrib.auth import logout
from core import views



# Create your views here.
def home(request):
    count_services = Service.get_services_count()
    count_customers = Customer.get_customers_count()
    count_appoint = Appointment.get_appoint_count()
    return render(request, 'dashboard/home.html', {'count_services': count_services, 'count_customers': count_customers, 'count_appoint': count_appoint})

def add_services(request):
    form = AddServiceForm
    if request.method == 'POST':
        form = AddServiceForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/dashboard/all_services/')
    else:
        form = AddServiceForm
    return render(request, 'dashboard/add_services.html', {'form': form})   

def edit_service(request, id):
    form = AddServiceForm
    if request.method == 'POST':
        service = Service.objects.get(pk=id)
        form = AddServiceForm(request.POST, request.FILES, instance=service)
        if form.is_valid():
            form.save()
            return redirect('all_services')
    else:
        service = Service.objects.get(pk=id)
        form = AddServiceForm(instance=service)
    return render(request, 'dashboard/edit_service.html', {'form': form})

def delete_service(request, id):
    if request.method == 'POST':
        service = Service.objects.get(pk=id)
        service.delete()
        return redirect('all_services')

def all_services(request):
	services = Service.get_all_services()
	return render(request, 'dashboard/all_services.html', {'services': services})      

def all_appointment(request):
    appointments = Appointment.objects.all()
    return render(request, 'dashboard/all_appointment.html', {'appointments': appointments})

def all_customers(request):
	customers = Customer.get_all_customers()
	return render(request, 'dashboard/all_customers.html', {'customers': customers})

def logoutAdmin(request):
    logout(request)
    return redirect('admin_login')
       
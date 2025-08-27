from django.shortcuts import render, redirect, HttpResponseRedirect
from django.contrib.auth.hashers import check_password, make_password
from dashboard.middlewares.auth import auth_middleware
from django.contrib.auth import authenticate, login as auth_login, logout
from django.contrib.auth.models import User
from django.utils.decorators import method_decorator 
from core.models import Service, Customer, Appointment
from core.views import *
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
# from dashboard.forms import AdminForm

# Create your views here.
def index(request):
	services = Service.get_all_services()
	return render(request, 'core/index.html', {'services' : services})

def services(request):
    services = Service.get_all_services()
    return render(request, 'core/services.html', {'services' : services})

def contact(request):
    return render(request, 'core/contact.html')

def about(request):
    return render(request, 'core/about.html')  

@auth_middleware
def appointments(request):
	customer = request.session.get('customer')
	appointments = Appointment.get_appointment_by_customer(customer)
	return render(request, 'core/appointments.html', {'appointments': appointments})

def bookappointment(request):
	services = Service.get_all_services()

	if request.method == 'GET':
		return render(request, 'core/bookappointment.html', {'services' : services})
	else:
		customer = request.session.get('customer')	
		your_name = request.POST.get('your-name')
		your_phone = request.POST.get('your-phone')
		your_email = request.POST.get('your-email')
		your_service = request.POST.get('your-service')
		your_date = request.POST.get('your-date')
	
		details = Appointment.objects.create(
			customer = Customer(id = customer),
		    your_name = your_name, 
		    your_phone = your_phone, 
		    your_email = your_email, 
		    your_service_id = your_service,
		    your_date = your_date
		)
		details.save()
		return render(request, 'core/bookappointment.html', {'services' : services})    

def signup(request):
	if request.method == 'GET':
		return render(request, 'core/signup.html')
	else:
		first_name = request.POST.get('fname')
		last_name = request.POST.get('lname')
		address = request.POST.get('address')
		phone = request.POST.get('phone')
		email = request.POST.get('email')
		password = request.POST.get('password')

		# Validation
		value = {
            'first_name': first_name,
            'last_name': last_name,
            'address': address,
            'phone': phone,
            'email': email
        }

		customer = Customer(first_name = first_name, last_name = last_name, address = address, phone = phone, email = email, password = password)
		
		error_msg = None
		# Saving
		if(not error_msg):
			customer.password = make_password(customer.password)
			customer.register()
			return redirect('index')
		else:
			data = {
				'error': error_msg,
				'values': value 
			}
			return render(request, 'core/signup.html', data)
	
def login(request):
	return_url = None
	if request.method == 'GET':
		login.return_url = request.GET.get('return_url')
		return render(request, 'core/login.html')
	else:
		email = request.POST.get('email')
		password = request.POST.get('password')
		customer = Customer.get_customer_by_email(email)
		error_msg = None
		if customer:
			flag = check_password(password, customer.password)
			if flag:
				request.session['customer'] = customer.id
				if login.return_url:
					return HttpResponseRedirect(Login.return_url)
				else:
					login.return_url = None
					return redirect('index')
			else:
				error_msg = 'Email or Password Invalid!!'
		else:
			error_msg = 'Email or Password Invalid!!' 
		return render(request, 'core/login.html', {'error': error_msg})

def logout(request):
    request.session.clear()
    return redirect('login')

def admin_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            auth_login(request, user)
            return redirect('home') 
    return render(request, 'core/admin_login.html')

def delete_service(request, id):
    print("🛠 DELETE VIEW HIT")
    print(f"Method: {request.method}, Service ID: {id}")
    
    if request.method == 'POST':
        service = get_object_or_404(Service, id=id)
        print(f"Deleting service: {service.name}")
        service.delete()
        return redirect('/dashboard/all_services/')
    
    print("❌ Not a POST request")
    return redirect('/dashboard/all_services/')

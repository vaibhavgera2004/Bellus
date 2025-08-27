from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings

# Create your models here.
class Service(models.Model):
    name = models.CharField(max_length=50)
    price = models.IntegerField(default=0)
    image = models.ImageField(upload_to='uploads/productImg')

    @staticmethod
    def get_all_services():
        return Service.objects.all()

    @staticmethod
    def get_services_count():
    	return Service.objects.count()


class Customer(models.Model):
	GenderChoice = (
        ("0","Male"),
        ("1","Female"),
        )

	first_name = models.CharField(max_length=20, null=True)
	last_name = models.CharField(max_length=20, null=True)
	address = models.CharField(max_length=500, null=True)
	phone = models.CharField(max_length=10, null=True)
	gender = models.IntegerField(choices=GenderChoice, default=1)
	email = models.CharField(max_length=100, null=True)
	password = models.CharField(max_length=8, null=True)

	def register(self):
		self.save()

	@staticmethod	
	def get_all_customers():
		return Customer.objects.all()

	@staticmethod
	def get_customers_count():
		return Customer.objects.count()	

	@staticmethod
	def get_customer_by_email(email):
		try:
			return Customer.objects.get(email = email)
		except:
			return False

	def isExists(self):
		if Customer.objects.filter(email = self.email):
			return True
		return False 	


class Appointment(models.Model):
	customer = models.ForeignKey(Customer, on_delete=models.CASCADE, null=True)
	your_name = models.CharField(max_length=100)
	your_phone = models.CharField(max_length=10)
	your_email = models.EmailField(max_length=200)
	your_service = models.ForeignKey('Service', on_delete=models.CASCADE, default=1)
	your_date = models.DateField()

	@staticmethod
	def get_all_appointments():
		return Appointment.objects.all()

	@staticmethod
	def get_appoint_count():
		return Appointment.objects.count()

	@staticmethod
	def get_appointment_by_customer(customer_id):
		return Appointment.objects.filter(customer = customer_id)


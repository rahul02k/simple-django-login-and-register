from django.db import models
from django.contrib.auth.models import User


class Activation(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    code = models.CharField(max_length=20, unique=True)
    email = models.EmailField(blank=True)


# declare a new model with a name "DashboardAdminModel"
class DashboardAdminModel(models.Model):
    # fields of the model
    member_id = models.CharField(max_length=200, default=None)
    account_id = models.CharField(max_length=200, default=None)
    name = models.CharField(max_length=200, default=None)
    phone_number = models.CharField(max_length=200, default=None)
    email_id = models.CharField(max_length=200, default=None)
    adhaar_card = models.CharField(max_length=200, default=None)
    pan_card = models.CharField(max_length=200, default=None)
    address = models.CharField(max_length=400, default=None)
    father_name = models.CharField(max_length=200, default=None)
    mother_name = models.CharField(max_length=200, default=None)
    date_of_birth = models.DateTimeField(default=None)
    last_modified = models.DateTimeField(auto_now_add=True)


# declare a new model with a name "DashboardCustomer"
class DashboardCustomer(models.Model):
    member_id = models.CharField(max_length=200, default=None)
    account_id = models.CharField(max_length=200, default=None)
    name = models.CharField(max_length=200, default=None)
    type_of_account = models.CharField(max_length=200, default=None)
    acc_balance = models.FloatField(default=None)
    interest = models.FloatField(default=None)
    money_paid = models.FloatField(default=None)
    date_of_opening = models.DateTimeField(default=None)
    date_of_maturity = models.DateTimeField(default=None)

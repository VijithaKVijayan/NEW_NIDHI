from django.contrib import admin
from django.contrib.auth.models import Group, User
from .models import Employee, Customer

# Register your models here.
admin.site.register(Employee)
admin.site.register(Customer)
admin.site.unregister(Group) 
admin.site.unregister(User) 
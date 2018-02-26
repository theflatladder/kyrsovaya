from django.contrib import admin
from .models import *

class UserAdmin(admin.ModelAdmin):
    list_display = ["name", "email"]



class Meta:
    model = UserRegistration


admin.site.register(UserRegistration, UserAdmin)
from django.contrib import admin

# from django.contrib.auth.admin import UserAdmin
from .models import User, Patient, Doctor, Profile

# from django.contrib.auth.forms import (
#     UserCreationForm,
#     UserChangeForm,
# )
# from django.contrib.admin.views.main import ChangeList
# from .forms import IllnessChangeForm

# Register your models here.


admin.site.register(User)
admin.site.register(Patient)
admin.site.register(Doctor)
admin.site.register(Profile)
# @admin.register(User)
# class UserAdmin(UserAdmin):
#     pass


# @admin.register(Patient)
# class PatientAdmin(UserAdmin):
#     readonly_fields = ("type",)


# @admin.register(Doctor)
# class DoctorAdmin(UserAdmin):
#     readonly_fields = ("type",)

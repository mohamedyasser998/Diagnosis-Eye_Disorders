from django.contrib import admin
from .models import Illness, Consults, Comment,Appointment  # , Medicine

# Register your models here.

admin.site.register(Illness)
admin.site.register(Consults)
admin.site.register(Comment)
# admin.site.register(Medicine)
admin.site.register(Appointment)

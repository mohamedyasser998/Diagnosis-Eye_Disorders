from django.contrib import admin
from .models import Illness, Symptom, Medicine

# Register your models here.

admin.site.register(Illness)
admin.site.register(Symptom)
admin.site.register(Medicine)

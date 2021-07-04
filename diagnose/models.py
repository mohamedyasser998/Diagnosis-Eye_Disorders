from django.db import models
from users.models import User

# Create your models here.


class Illness(models.Model):
    Name = models.CharField(max_length=30, unique=True)
    Severity = models.CharField(max_length=30)
    User = models.ManyToManyField(User, null=True, blank=True)


class Symptom(models.Model):
    Name = models.CharField(max_length=30, unique=True)
    Severity = models.CharField(max_length=30)
    Illness = models.ManyToManyField(Illness)
    User = models.ManyToManyField(User, null=True, blank=True)


# ====================================================
class IntegerRangeField(models.IntegerField):
    def __init__(
        self, verbose_name=None, name=None, min_value=None, max_value=None, **kwargs
    ):
        self.min_value, self.max_value = min_value, max_value
        models.IntegerField.__init__(self, verbose_name, name, **kwargs)

    def formfield(self, **kwargs):
        defaults = {"min_value": self.min_value, "max_value": self.max_value}
        defaults.update(kwargs)
        return super(IntegerRangeField, self).formfield(**defaults)


class Medicine(models.Model):
    Name = models.CharField(max_length=30, unique=True)
    Dosage = IntegerRangeField(min_value=1, max_value=24)
    Symptom = models.ManyToManyField(Symptom)
    User = models.ManyToManyField(User, null=True, blank=True)

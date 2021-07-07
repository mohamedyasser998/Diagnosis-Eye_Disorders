from django.db import models

from diagnose.models import Illness  # , Medicine

# from django.urls import reverse
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.contrib.auth.base_user import BaseUserManager
from django.utils.translation import ugettext_lazy as _

# from django.utils import timezone

# from django.conf import settings
# from django.db.models.signals import post_save

# from django.dispatch import receiver


class UserManager(BaseUserManager):

    """Custom user model where (((field = email))) is the unique identifier for authentication"""

    def create_user(self, email, password, **extra_fields):
        "Create and save User in DB with the given email and password"

        if not email:
            raise ValueError(_("The Email must be set"))
        if not password:
            raise ValueError(_("The Password must be set"))

        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password, **extra_fields):
        """Create and save SuperUser in DB with the given email and password"""

        extra_fields.setdefault("is_superuser", True)
        extra_fields.setdefault("is_active", True)
        extra_fields.setdefault("is_staff", True)

        if extra_fields.get("is_superuser") is not True:
            raise ValueError(_("Super User must have is_superuser=True."))
        if extra_fields.get("is_staff") is not True:
            raise ValueError(_("Super User must have is_staff=True."))
        return self.create_user(email, password, **extra_fields)


# ================== User Model
class User(AbstractBaseUser, PermissionsMixin):
    class Types(models.TextChoices):
        DOCTOR = "DOCTOR", "Doctor"
        PATIENT = "PATIENT", "Patient"

    type = models.CharField(
        _("Type"), max_length=50, choices=Types.choices, default=Types.PATIENT
    )

    email = models.EmailField(_("email address"), unique=True)
    first_name = models.CharField(_("first name"), max_length=30, blank=True)
    last_name = models.CharField(_("last name"), max_length=30, blank=True)
    illness = models.ManyToManyField(Illness, blank=True)
    # medicine = models.ManyToManyField(Medicine)
    is_active = models.BooleanField(_("active"), default=True)
    is_staff = models.BooleanField(_("is staff"), default=False)
    # admin = models.BooleanField(_("is admin"), default=False)
    # date_joined = models.DateTimeField(_("date joined"), default=timezone.now)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["first_name", "last_name"]

    objects = UserManager()

    class Meta:
        verbose_name = _("User")
        verbose_name_plural = _("Users")

    def __str__(self):
        return self.email

    def get_full_name(self):
        """Return Full name with a space between them"""

        full_name = "%s %s" % (self.first_name, self.last_name)
        return full_name.strip()


# ==================  User Profile
# class Profile(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE)

#     def __str__(self):
#         return str(self.user)

#     def get_absolute_url(self):
#         return reverse("home")


# ==================  Receiver to create/update when create/update user instance
# @receiver(post_save, sender=settings.AUTH_USER_MODEL)
# def create_user_profile(sender, instance, created, **kwargs):
#     if created:
#         Profile.objects.create(user=instance)


# @receiver(post_save, sender=User)
# def save_user_profile(sender, instance, **kwargs):
#     instance.profile.save()


# Without Manager filtering users by their type doesn't work all users have both types
# ==================  ModelManager 2
class PatientManager(models.Manager):
    def get_queryset(self, *args, **kwargs):
        return super().get_queryset(*args, **kwargs).filter(type=User.Types.PATIENT)


class DoctorManager(models.Manager):
    def get_queryset(self, *args, **kwargs):
        return super().get_queryset(*args, **kwargs).filter(type=User.Types.DOCTOR)


# ==================  User Model 2
class Patient(User):
    objects = PatientManager()

    class Meta:
        proxy = True
        # ordering = ('..')

    def save(self, *args, **kwargs):
        if not self.pk:
            self.type = User.Types.PATIENT
        return super().save(*args, **kwargs)


class Doctor(User):
    objects = DoctorManager()

    class Meta:
        proxy = True
        # ordering = ('..')

    def save(self, *args, **kwargs):
        if not self.pk:
            self.type = User.Types.DOCTOR
        return super().save(*args, **kwargs)

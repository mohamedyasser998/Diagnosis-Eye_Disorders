from django.db import models

# from django.db.models.enums import Choices

# from users.models import User
from multiselectfield import MultiSelectField
from django.utils.translation import ugettext_lazy as _

# from users.models import User

MY_CHOICES = (
    ("None", "None"),
    (
        "gradual or sudden change in the quality of your vision followed by appearance of straight lines as distorted",
        "gradual or sudden change in the quality of your vision followed by appearance of straight lines as distorted",
    ),
    ("Blurriness of central vision", "Blurriness of central vision"),
    (
        "Partial vision loss marked by formation of blind spots (scotomas)",
        "Partial vision loss marked by formation of blind spots (scotomas)",
    ),
    ("Problem seeing in dim light", "Problem seeing in dim light"),
    (
        "Objects appearing smaller than their actual size,as viewed with one eye and then the other",
        "Objects appearing smaller than their actual size,as viewed with one eye and then the other",
    ),
    (
        "lacking typical symptoms like pain,tearing or redness of eyes",
        "lacking typical symptoms like pain,tearing or redness of eyes",
    ),
    ("Blurred clouded or dim vision", "Blurred clouded or dim vision"),
    ("Problem seeing at night", "Problem seeing at night"),
    (
        "Problem seeing through light and glare",
        "Problem seeing through light and glare",
    ),
    ("Seeing halos around lights", "Seeing halos around lights"),
    (
        "Frequently changing contact lens prescription or eyeglasses",
        "Frequently changing contact lens prescription or eyeglasses",
    ),
    ("Faded view of colors", "Faded view of colors"),
    ("Tunnel vision", "Tunnel vision"),
    (
        "Peripheral vision loss gradually affecting both eyes in most cases",
        "Peripheral vision loss gradually affecting both eyes in most cases",
    ),
    (
        "Severe pain in eyes accompanied by nausea and vomiting in most cases",
        "Severe pain in eyes accompanied by nausea and vomiting in most cases",
    ),
    (
        "Sudden visual disturbance in low light conditions",
        "Sudden visual disturbance in low light conditions",
    ),
    ("Halos around lights", "Halos around lights"),
    ("Redness of the eyes", "Redness of the eyes"),
)


class Illness(models.Model):
    Name = models.CharField(max_length=300, unique=True)

    class Severities(models.TextChoices):
        LOW = "LOW", "Low"
        MINOR = "MINOR", "Minor"
        SIGNIFICANT = "SIGNIFICANT", "Significant"
        CRITICAL = "CRITICAL", "Critical"

    Severity = models.CharField(
        _("Severity"),
        max_length=50,
        choices=Severities.choices,
        default=Severities.MINOR,
    )
    Treatement = models.TextField(null=True, blank=True)
    Symptom = MultiSelectField(choices=MY_CHOICES, null=True)

    def __str__(self):
        return self.Name


class Consults(models.Model):
    user = models.ForeignKey("users.User", on_delete=models.CASCADE)
    symptoms = models.TextField(null=True, blank=True)
    illness = models.ForeignKey(
        Illness, on_delete=models.CASCADE, related_name="illness", default="5"
    )

    def __str__(self):
        return str(self.user)

    def split_symptoms(self):
        return self.symptoms.split(",")


class Comment(models.Model):
    post = models.ForeignKey(
        Consults, related_name="comments", on_delete=models.CASCADE
    )
    author = models.ForeignKey("users.User", on_delete=models.CASCADE)
    body = models.TextField(null=True, blank=True)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "%s - %s" % (self.post, self.author)


class Appointment(models.Model):
    date = models.DateField()
    time = models.TimeField()
    status = models.CharField(
        choices=[("Pending", "Pending"), ("Completed", "Completed")], max_length=10
    )
    patient = models.ForeignKey(
        "users.User", on_delete=models.CASCADE, related_name="patient"
    )
    doctor = models.ForeignKey(
        "users.User", on_delete=models.CASCADE, related_name="doctor"
    )

    def __str__(self):
        return "Patient - {} Doc- {} At {} {}".format(
            self.patient, self.doctor, self.date, self.time
        )

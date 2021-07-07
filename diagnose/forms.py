# from django.contrib.auth.forms import
from django import forms

# from django.forms import widgets

# from django.forms import widgets
# from django.forms.widgets import Select
# from django.forms import ModelForm

from .models import Consults, Comment, MY_CHOICES,Appointment
from users.models import User


# choices = [MY_CHOICES]
# choices_list = []
# for item in choices:
#     choices_list.append(item)


class CheckSymptomsForm(forms.ModelForm):
    symptoms = forms.MultipleChoiceField(
        widget=forms.CheckboxSelectMultiple,
        choices=MY_CHOICES,
        label="",
    )

    class Meta:
        model = Consults
        fields = (
            "user",
            "symptoms",
        )
        widgets = {
            "user": forms.HiddenInput(),
        }


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ("author", "body")

        widgets = {
            "author": forms.HiddenInput(),
            "body": forms.Textarea(
                attrs={"class": "form-control", "rows": 2, "cols": 10}
            ),
        }

class DiagnosisForm(forms.ModelForm):
    symptoms = forms.MultipleChoiceField(
        widget=forms.CheckboxSelectMultiple,
        choices=MY_CHOICES,
        label="",
    )

    class Meta:
        model = Consults
        fields = (
            "user",
            "symptoms",
        )
        widgets = {
            "user": forms.HiddenInput(),
        }
class AppointmentForm(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = "__all__"
        widgets = {
            "patient": forms.HiddenInput(),
            # "doctor": forms.HiddenInput(),
        }

    def __init__(self, *args, **kwargs):
        super(AppointmentForm, self).__init__(*args, **kwargs)
        if self.instance:
            # self.fields['patient'].queryset = User.objects.filter(user_type="P")
            self.fields["doctor"].queryset = User.objects.filter(type="DOCTOR")
            self.fields["date"].label = "Date (YYYY-MM-DD)"
            self.fields["time"].label = "Time 24 hr (HH:MM)"

# from django.contrib.auth.forms import
from django import forms

# from django.forms import widgets

# from django.forms import widgets
# from django.forms.widgets import Select
# from django.forms import ModelForm

from .models import Consults, Comment, MY_CHOICES  # , Medicine


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
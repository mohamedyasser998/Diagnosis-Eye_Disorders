from django.contrib.auth.forms import UserCreationForm
from django import forms

# from django.forms import widgets
# from django.forms.widgets import Select
from .models import User, Profile
from phonenumber_field.formfields import PhoneNumberField


choices = [
    ("Allergy and immunology", "Allergy and immunology"),
    ("Anesthesiology", "Anesthesiology"),
    ("Dermatology", "Dermatology"),
    ("Diagnostic radiology", "Diagnostic radiology"),
    ("Neurology", "Neurology"),
    ("Pathology", "Pathology"),
    ("Pediatrics", "Pediatrics"),
    ("Surgery", "Surgery"),
]
choices_list = []
for item in choices:
    choices_list.append(item)


class SignUpForm(UserCreationForm):
    email = forms.EmailField(widget=forms.EmailInput(attrs={"class": "form-control"}))
    first_name = forms.CharField(
        max_length=100, widget=forms.TextInput(attrs={"class": "form-control"})
    )
    last_name = forms.CharField(
        max_length=100, widget=forms.TextInput(attrs={"class": "form-control"})
    )

    class Meta:
        model = User
        fields = ("first_name", "last_name", "email", "password1", "password2")

    def __init__(self, *args, **kwargs):
        super(SignUpForm, self).__init__(*args, **kwargs)
        self.fields["password1"].widget.attrs["class"] = "form-control"
        self.fields["password2"].widget.attrs["class"] = "form-control"


class EditProfileForm(forms.ModelForm):
    email = forms.EmailField(widget=forms.EmailInput(attrs={"class": "form-control"}))
    first_name = forms.CharField(
        max_length=100, widget=forms.TextInput(attrs={"class": "form-control"})
    )
    last_name = forms.CharField(
        max_length=100, widget=forms.TextInput(attrs={"class": "form-control"})
    )
    bio = forms.CharField(
        widget=forms.Textarea(attrs={"class": "form-control", "rows": 2, "cols": 5}),
        required=False,
    )
    phone_number = PhoneNumberField()
    facebook_url = forms.CharField(
        widget=forms.TextInput(attrs={"class": "form-control"}), required=False
    )
    twitter_url = forms.CharField(
        widget=forms.TextInput(attrs={"class": "form-control"}), required=False
    )
    instagram_url = forms.CharField(
        widget=forms.TextInput(attrs={"class": "form-control"}), required=False
    )
    academic_Title = forms.CharField(
        widget=forms.TextInput(attrs={"class": "form-control"}), required=False
    )
    employment_history = forms.CharField(
        widget=forms.Textarea(attrs={"class": "form-control", "rows": 2, "cols": 10}),
        required=False,
    )
    experience = forms.CharField(
        widget=forms.Textarea(attrs={"class": "form-control", "rows": 2, "cols": 10}),
        required=False,
    )
    speciality = forms.MultipleChoiceField(
        label=u"Select Your Specialities",
        choices=choices_list,
        widget=forms.CheckboxSelectMultiple(),
        required=False,
    )

    class Meta:
        model = Profile
        fields = (
            "first_name",
            "last_name",
            "email",
            "bio",
            "phone_number",
            "profile_pic",
            "facebook_url",
            "twitter_url",
            "instagram_url",
            "academic_Title",
            "employment_history",
            "experience",
            "speciality",
        )

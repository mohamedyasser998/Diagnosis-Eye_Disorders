# from django.shortcuts import render
from django.views.generic import CreateView, ListView, DetailView
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from django.views import generic
from django.urls import reverse


from .forms import SignUpForm, EditProfileForm
from .models import Doctor, Profile

# Create your views here.


class SignUpView(CreateView):
    form_class = SignUpForm
    success_url = reverse_lazy("login")
    template_name = "registration/signup.html"


class AboutView(ListView):
    model = Doctor
    template_name = "about.html"
    ordering = ["-id"]


class ShowProfileView(DetailView):
    model = Profile
    template_name = "user_profile.html"

    def get_context_data(self, *args, **kwargs):
        context = super(ShowProfileView, self).get_context_data(*args, **kwargs)
        page_user = get_object_or_404(Profile, id=self.kwargs["pk"])
        context["page_user"] = page_user
        return context


class EditProfilePageView(generic.UpdateView):
    model = Profile
    template_name = "edit_profile.html"
    form_class = EditProfileForm

    def get_success_url(self):
        pk = self.kwargs["pk"]
        return reverse("users:show_profile", kwargs={"pk": pk})

    def get_initial(self):
        initial = super().get_initial()
        initial["first_name"] = self.request.user.first_name
        initial["last_name"] = self.request.user.last_name
        initial["email"] = self.request.user.email
        return initial

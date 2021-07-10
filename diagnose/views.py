from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect  # , get_object_or_404
from django.urls import reverse

from django.views.generic import CreateView, ListView, DetailView  # , UpdateView
from .models import Consults, Comment, Illness, Appointment
from .forms import (
    CheckSymptomsForm,
    CommentForm,
    DiagnosisForm,
    AppointmentForm,
)
from django.contrib import messages

# from django.http import HttpResponse


def homePageView(request):
    return render(request, "home.html")


class CheckSymptoms(CreateView):
    model = Consults
    form_class = CheckSymptomsForm
    template_name = "symptoms.html"

    def get_success_url(self):
        return reverse("diagnose:home")

    def get_initial(self):
        initial = super().get_initial()
        # consultee = User.objects.get(id=self.request.user.id)
        initial["user"] = self.request.user
        return initial

    def form_valid(self, form):
        for j in range(len(Illness.objects.all())):
            queryset_list = Illness.objects.values()

            q = list(queryset_list)
            name = q[j]["Name"]
            q[j]["Name"] = list(q[j]["Symptom"])
            count = 0
            for i in range(len(form.cleaned_data["symptoms"])):
                if form.cleaned_data["symptoms"][i] in q[j]["Name"]:
                    count += 1
            if count > len(q[j]["Name"]) / 2:
                print(len(q[j]["Name"]))
                print(count)
                form.instance.illness = Illness.objects.get(Name=str(name))
                return super().form_valid(form)
            else:
                form.instance.illness = Illness.objects.get(Name="None")
                return super().form_valid(form)
                # return str(name)


class ConsultsListView(ListView):
    models = Consults
    template_name = "consults.html"
    # ordering = ["id"]

    def get_queryset(self):
        return Consults.objects.all()


class ConsultDetailView(DetailView):
    model = Consults
    template_name = "consult_detail.html"


class CommentCreateView(CreateView):
    model = Comment
    form_class = CommentForm
    template_name = "add_comment.html"

    def form_valid(self, form):
        form.instance.post_id = self.kwargs["pk"]
        return super().form_valid(form)

    def get_success_url(self):
        pk = self.kwargs["pk"]
        return reverse("diagnose:post_detail", kwargs={"pk": pk})

    def get_initial(self):
        initial = super().get_initial()
        initial["author"] = self.request.user
        return initial


class DiagnosisCreateView(LoginRequiredMixin, CreateView):
    login_url = "/users/login/"
    model = Illness
    form_class = DiagnosisForm
    template_name = "diagnosis.html"
    # success_url = reverse_lazy("AppointmentCreateView")

    def get_initial(self):
        initial = super().get_initial()
        # consultee = User.objects.get(id=self.request.user.id)
        initial["user"] = self.request.user
        return initial

    def post(self, request, *args, **kwargs):
        form = DiagnosisForm(request.POST)
        if form.is_valid():
            for j in range(len(Illness.objects.all())):
                queryset_list = Illness.objects.values()

                q = list(queryset_list)
                name = q[j]["Name"]
                q[j]["Name"] = list(q[j]["Symptom"])
                print(q[j]["Name"])
                count = 0
                for i in range(len(form.cleaned_data["symptoms"])):
                    # print(form.cleaned_data['symptoms'])
                    if form.cleaned_data["symptoms"][i] in q[j]["Name"]:
                        count += 1
                if count > len(q[j]["Name"]) / 2:
                    print(len(q[j]["Name"]))
                    print(count)
                    messages.success(request, "you might have " + str(name))
                    return redirect("/diag/")
        messages.success(request, "Appointment done successfully")
        return redirect("/diag/")


class AppointmentCreateView(LoginRequiredMixin, CreateView):
    login_url = "/users/login/"
    model = Appointment
    form_class = AppointmentForm
    template_name = "appointment_create.html"
    # success_url = reverse_lazy("AppointmentCreateView")

    def get_initial(self):
        initial = super().get_initial()
        initial["patient"] = self.request.user
        # initial["doctor"] = User.objects.get(pk=self.kwargs["pk"])
        return initial

    def post(self, request, *args, **kwargs):
        form = AppointmentForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Appointment done successfully")
            return redirect("/appointment/create")


class AppointmentsForAPatientView(LoginRequiredMixin, ListView):
    login_url = "/users/login/"
    # redirect_field_name = 'login'
    template_name = "appointment_list.html"

    def get_queryset(self):
        return Appointment.objects.filter(patient=self.request.user)


class AppointmentsForADoctorView(LoginRequiredMixin, ListView):
    login_url = "/users/login/"
    redirect_field_name = "account:login"
    template_name = "appointment_list_Doctor.html"

    def get_queryset(self):
        return Appointment.objects.filter(doctor=self.request.user)

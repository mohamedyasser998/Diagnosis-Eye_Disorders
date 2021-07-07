from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect  # , get_object_or_404
from django.urls import reverse

from django.views.generic import CreateView, ListView, DetailView  # , UpdateView
from .models import Consults, Comment , Illness  # , Medicine
from .forms import CheckSymptomsForm, CommentForm, DiagnosisForm
from django.contrib import messages
from django.http import HttpResponse



# from users.models import User


# from django.http import HttpResponse

# Create your views here.


def homePageView(request):
    return render(request, "home.html")


class CheckSymptoms(CreateView):
    model = Consults
    form_class = CheckSymptomsForm
    template_name = "symptoms.html"

    def get_success_url(self):
        return reverse("home")

    def get_initial(self):
        initial = super().get_initial()
        # consultee = User.objects.get(id=self.request.user.id)
        initial["user"] = self.request.user
        return initial


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
        return reverse("post_detail", kwargs={"pk": pk})

    def get_initial(self):
        initial = super().get_initial()
        initial["author"] = self.request.user
        return initial

# def Diagnosis(request):
#
#     if request.method == 'POST': # If the form has been submitted...
#         form = DiagnosisForm(request.POST) # A form bound to the POST data
#         if form.is_valid(): # All validation rules pass
#
#             print(form.cleaned_data['symptoms'])
#
#             # return HttpResponseRedirect('/thanks/') # Redirect after POST
#     else:
#         form = DiagnosisForm() # An unbound form
#
#         return reverse("home")
#

desis1 = ["Faded view of colors", "Tunnel vision", "cherry"]

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

    # def get_queryset(self, request, *args, **kwargs):
    #     queryset_list = Illness.objects.all()
    #     print(len(queryset_list))
    #     messages.success(request,'There are {count} articles.'.format(count=len(Illness.objects.all())))

    def post(self, request, *args, **kwargs):
        form = DiagnosisForm(request.POST)
        if form.is_valid():
            for j in range(len(Illness.objects.all())):
              queryset_list = Illness.objects.values()

              q = list(queryset_list)
              name = q[j]["Name"]
              q[j]["Name"] = list(q[j]["Symptom"])
              # print(q[j]["Name"])
              count = 0
              for i in range(len(form.cleaned_data['symptoms'])):
                  # print(form.cleaned_data['symptoms'])
                  if form.cleaned_data['symptoms'][i] in  q[j]["Name"] :
                      count +=1
              if count > len(q[j]["Name"])/2 :
               print(len(q[j]["Name"]))
               print(count)
               messages.success(request, "you might have "+ str(name) )
               return redirect("/diag/")
        # queryset_list = Illness.objects.values()
        # q=list(queryset_list)
        # print(q[2]["Name"])
        # q[2]["Name"]=list(q[2]["Symptom"])
        # print(q[2]["Name"])
        # messages.success(request, 'There are {count} Illness.'.format(count=len(Illness.objects.all())))
        messages.success(request, "Appointment done successfully")
        return redirect("/diag/")
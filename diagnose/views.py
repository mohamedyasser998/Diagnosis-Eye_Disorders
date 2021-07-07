from django.shortcuts import render  # , get_object_or_404
from django.urls import reverse

from django.views.generic import CreateView, ListView, DetailView  # , UpdateView
from .models import Consults, Comment  # , Illness  # , Medicine
from .forms import CheckSymptomsForm, CommentForm

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

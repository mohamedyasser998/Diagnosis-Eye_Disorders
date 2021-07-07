from django.urls import path

from .views import (
    homePageView,
    CheckSymptoms,
    ConsultsListView,
    ConsultDetailView,
    CommentCreateView,
DiagnosisCreateView
)

urlpatterns = [
    path("", homePageView, name="home"),
    path("diagnose/", CheckSymptoms.as_view(), name="check_symptoms"),
    path("posts", ConsultsListView.as_view(), name="posts"),
    path("posts/<int:pk>/", ConsultDetailView.as_view(), name="post_detail"),
    path("posts/<int:pk>/comment/", CommentCreateView.as_view(), name="add_comment"),
    path("diag/",DiagnosisCreateView.as_view(), name="check_diagnosis")
]

from django.urls import path

from .views import (
    homePageView,
    CheckSymptoms,
    ConsultsListView,
    ConsultDetailView,
    CommentCreateView,
DiagnosisCreateView,
AppointmentCreateView,
AppointmentsForADoctorView,
AppointmentsForAPatientView
)

urlpatterns = [
    path("", homePageView, name="home"),
    path("diagnose/", CheckSymptoms.as_view(), name="check_symptoms"),
    path("posts", ConsultsListView.as_view(), name="posts"),
    path("posts/<int:pk>/", ConsultDetailView.as_view(), name="post_detail"),
    path("posts/<int:pk>/comment/", CommentCreateView.as_view(), name="add_comment"),
    path("diag/",DiagnosisCreateView.as_view(), name="check_diagnosis"),
    path("appointment/create", AppointmentCreateView.as_view(), name="appointment-create"),
path(
        "appointment/p/",AppointmentsForAPatientView.as_view(),
        name="patient-appointments",
    ),
    path(
        "appointment/d/",AppointmentsForADoctorView.as_view(),
        name="doctor-appointments",
    ),
]

from django.urls import path
from .views import SignUpView, AboutView, ShowProfileView, EditProfilePageView

# from .views import
app_name = "users"

urlpatterns = [
    path("signup/", SignUpView.as_view(), name="signup"),
    path("about/", AboutView.as_view(), name="about"),
    path("<int:pk>/profile", ShowProfileView.as_view(), name="show_profile"),
    path(
        "<int:pk>/edit_profile",
        EditProfilePageView.as_view(),
        name="edit_profile",
    ),
]

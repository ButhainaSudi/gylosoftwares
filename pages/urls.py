from django.urls import path

from . import views

app_name = "pages"

urlpatterns = [
    path("", views.home, name="home"),
    path("about/", views.about, name="about"),
    path("industries/", views.industries, name="industries"),
    path("privacy-policy/", views.privacy, name="privacy"),
    path("terms-of-service/", views.terms, name="terms"),
]

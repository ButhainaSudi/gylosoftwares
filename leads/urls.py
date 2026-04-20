from django.urls import path

from . import views

app_name = "leads"

urlpatterns = [
    path("contact/", views.contact, name="contact"),
    path("contact/success/", views.contact_success, name="contact_success"),
    path("start-project/", views.start_project, name="start_project"),
    path("start-project/success/", views.start_project_success, name="start_project_success"),
]

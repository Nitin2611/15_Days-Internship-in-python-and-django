from django.urls import path
from . import views

urlpatterns = [
    path("",views.homepage , name="Home"),
    path("about", views.aboutpage, name = "about"),
    path("contact",views.contactpage, name = "contact"),
    path("form",views.form, name = "form" ),
    path("formprocess",views.process, name = "process"),
    path("studentlist",views.Studentlist.as_view(), name = "s1"),
]  
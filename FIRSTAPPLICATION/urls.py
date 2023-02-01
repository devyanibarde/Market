from FIRSTAPPLICATION import views
from django.urls import path

urlpatterns = [
    path("", views.index),
    path("index", views.index1, name="header"),
    path("customers", views.customers, name="allcust"),
    path("orders", views.vieworders, name="order"),
]
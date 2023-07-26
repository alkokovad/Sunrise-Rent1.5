from django.urls import path
from . import views


urlpatterns = [
    path('', views.RentServiceView.as_view(), name="rentservice")
]
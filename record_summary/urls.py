from django.urls import path
from . import views

urlpatterns = [
    path('', views.check_record_summary, name="record_summary"),
]
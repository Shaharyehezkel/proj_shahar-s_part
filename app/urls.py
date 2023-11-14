from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('appointments/', views.AppointmentListCreateView.as_view()),
    path('appointments/<int:pk>/', views.AppointmentDetailView.as_view()),
]

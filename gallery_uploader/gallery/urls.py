from django.urls import path

from . import views

urlpatterns = [
    path('upload', views.SubmitImage.as_view()),
    path('list', views.imageView.as_view()),
    path("", views.SubmitImage.as_view())
]
from django.urls import path

from . import views

urlpatterns = [
    path('upload', views.SubmitImage.as_view()),
    path('list', views.image_list, name='list'),
    path("", views.SubmitImage.as_view()),
    path('gallery/list/<int:pk>',views.image_detail, name='detail')
]
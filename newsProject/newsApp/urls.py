from django.urls import path
from . import views

urlpatterns = [
    path('', views.HomePage, name = "HomePage"),
    path('post/view/<int:pk>/', views.postDetail, name = "postDetail"),
]

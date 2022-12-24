from django.urls import path
from . import views

urlpatterns = [
    path('toCollege',views.toCollege),
    path('toHome',views.toHome),
]
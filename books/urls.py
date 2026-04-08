from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='books.home'),
    path('<int:id>/', views.show, name='books.show'),
]

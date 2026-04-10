from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="authors.index"),
    path("create/", views.create_author, name="authors.create"),
    path("<int:id>/", views.show, name="authors.show"),
    path("<int:id>/update/", views.update_author, name="authors.update"),
    path("<int:id>/delete/", views.delete_author, name="authors.delete"),
]

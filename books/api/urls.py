from django.urls import path
from books.api.views import book_operations, books_list_create

urlpatterns = [
    path("", books_list_create, name="api.books.list_create"),
    path("<int:pk>/", book_operations, name="api.books.operations"),
]

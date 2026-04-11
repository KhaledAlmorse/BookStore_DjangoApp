from django.urls import include, path
from . import views

urlpatterns = [
    path('', views.home, name='books.home'),
    path('api/', include('books.api.urls')),
    path('admin/', views.admin_books, name='books.admin'),
    path('create/', views.create_book, name='books.create'),
    path('<int:id>/', views.show, name='books.show'),
    path('<int:id>/update/', views.update_book, name='books.update'),
    path('<int:id>/delete/', views.delete_book, name='books.delete'),
]

from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from books.models import Book
from books.api.serializers import bookModelSerializer


@api_view(["GET", "POST"])
def books_list_create(request):
    if request.method == "GET":
        books = Book.objects.all()
        serializer = bookModelSerializer(books, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    serializer = bookModelSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["GET", "PUT", "DELETE"])
def book_operations(request, pk):
    book = get_object_or_404(Book, pk=pk)
    print(request.method, "request received for book with id:", pk)
    if request.method == "GET":
        serializer = bookModelSerializer(book)
        return Response(serializer.data, status=status.HTTP_200_OK)

    elif request.method == "PUT":
        serializer = bookModelSerializer(book, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == "DELETE":
        print("Deleting book with id:", pk)
        book.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

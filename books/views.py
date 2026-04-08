from django.shortcuts import render, get_object_or_404, redirect
from books.models import Book
from books.forms import BookForm


# Create your views here.
def home(request):
    books = Book.objects.all()
    return render(request, "books/index.html", context={"books": books})


def index(request):
    books = Book.objects.all()
    return render(request, "books/index.html", context={"books": books})


def show(request, id):
    book = get_object_or_404(Book, id=id)
    return render(request, "books/show.html", context={"book": book})


def admin_books(request):
    books = Book.objects.all().order_by("id")
    return render(request, "books/admin.html", context={"books": books})


def create_book(request):
    if request.method == "POST":
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("books.admin")
    else:
        form = BookForm()

    return render(
        request,
        "books/form.html",
        context={"form": form, "form_title": "Create Book", "submit_label": "Create"},
    )


def update_book(request, id):
    book = get_object_or_404(Book, id=id)

    if request.method == "POST":
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect("books.admin")
    else:
        form = BookForm(instance=book)

    return render(
        request,
        "books/form.html",
        context={"form": form, "form_title": f"Update {book.title}", "submit_label": "Update"},
    )


def delete_book(request, id):
    book = get_object_or_404(Book, id=id)

    if request.method == "POST":
        book.delete()

    return redirect("books.admin")

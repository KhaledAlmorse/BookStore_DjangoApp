from django.shortcuts import render, get_object_or_404, redirect

from books.forms import BookForm
from books.models import Book


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
    form = BookForm()
    if request.method == "POST":
        form = BookForm(request.POST, request.FILES)
        if form.is_valid():  
            book = Book()
            book.title = form.cleaned_data["title"]
            book.brief = form.cleaned_data["brief"]
            book.image = form.cleaned_data["image"]
            book.no_of_pages = form.cleaned_data["no_of_pages"]
            book.price = form.cleaned_data["price"]
            book.save()
            return redirect("books.admin")
    return render(
        request,
        "books/form.html",
        context={"form": form, "form_title": "Create Book", "submit_label": "Create"}
    )


def update_book(request, id):
    book = get_object_or_404(Book, id=id)

    form = BookForm(initial={
        "title": book.title,
        "brief": book.brief,
        "no_of_pages": book.no_of_pages,
        "price": book.price,
    })

    if request.method == "POST":
        form = BookForm(request.POST, request.FILES)
        print(request.POST)  
        print(request.FILES)  
        if form.is_valid():  
            print(form.cleaned_data)
            book.title = form.cleaned_data["title"]
            book.brief = form.cleaned_data["brief"]
            book.image = form.cleaned_data["image"]
            book.no_of_pages = form.cleaned_data["no_of_pages"]
            book.price = form.cleaned_data["price"]
            if form.cleaned_data["image"]:
                book.image = form.cleaned_data["image"]
            book.save()
            return redirect("books.admin")

    return render(
        request,
        "books/form.html",
        context={"form": form, "form_title": "Update Book", "submit_label": "Update"}
    )


def delete_book(request, id):
    book = get_object_or_404(Book, id=id)
    if request.method == "POST":
        book.delete()
    return redirect("books.admin")
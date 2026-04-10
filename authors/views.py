from django.shortcuts import get_object_or_404, redirect, render

from authors.forms import AuthorModelForm
from authors.models import Author


def index(request):
    authors = Author.objects.all().order_by("-id")
    return render(request, "authors/index.html", context={"authors": authors})


def show(request, id):
    author = get_object_or_404(Author.objects.prefetch_related("books"), id=id)
    return render(request, "authors/show.html", context={"author": author})


def create_author(request):
    form = AuthorModelForm()
    if request.method == "POST":
        form = AuthorModelForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("authors.index")
    return render(
        request,
        "authors/form.html",
        context={"form": form, "form_title": "Create Author", "submit_label": "Create"},
    )


def update_author(request, id):
    author = get_object_or_404(Author, id=id)

    form = AuthorModelForm(instance=author)
    if request.method == "POST":
        form = AuthorModelForm(request.POST, request.FILES, instance=author)
        if form.is_valid():
            form.save()
            return redirect("authors.index")
    return render(
        request,
        "authors/form.html",
        context={"form": form, "form_title": "Update Author", "submit_label": "Update"},
    )


def delete_author(request, id):
    author = get_object_or_404(Author, id=id)
    if request.method == "POST":
        author.delete()
    return redirect("authors.index")

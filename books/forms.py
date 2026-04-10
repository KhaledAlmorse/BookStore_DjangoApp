from django import forms
from authors.models import Author

from books.models import Book


class BookModelForm(forms.ModelForm):
    authors = forms.ModelMultipleChoiceField(
        queryset=Author.objects.all().order_by("name"),
        required=True,
        widget=forms.SelectMultiple(attrs={"class": "author-select"}),
    )

    class Meta:
        model = Book
        fields = ["title", "brief", "image", "no_of_pages", "price", "authors"]

    def clean_title(self):
        title = self.cleaned_data["title"]
        if len(title.strip()) < 3:
            raise forms.ValidationError("Title must be at least 3 characters.")
        return title

    def clean_brief(self):
        brief = self.cleaned_data["brief"]
        if not brief.strip():
            raise forms.ValidationError("Brief must not be empty.")
        return brief

    def clean_no_of_pages(self):
        no_of_pages = self.cleaned_data["no_of_pages"]
        if no_of_pages <= 0:
            raise forms.ValidationError("No of pages must be greater than 0.")
        return no_of_pages

    def clean_price(self):
        price = self.cleaned_data["price"]
        if price <= 0:
            raise forms.ValidationError("Price must be greater than 0.")
        return price

from django import forms

from books.models import Book


class BookForm(forms.Form):
    """ each field defined in the form class, translate to html elements ? label , input , error """
    title = forms.CharField(max_length=255)
    brief = forms.CharField(widget=forms.Textarea)
    image = forms.ImageField(required=False)
    no_of_pages = forms.IntegerField()
    price = forms.DecimalField(max_digits=10, decimal_places=2)

    def clean_title(self):
        title = self.cleaned_data['title']
        if len(title.strip()) < 3:
            raise forms.ValidationError("Title must be at least 3 characters")
        return title

    def clean_brief(self):
        brief = self.cleaned_data['brief']
        if len(brief.strip()) == 0:
            raise forms.ValidationError("Brief must not be empty")
        return brief

    def clean_no_of_pages(self):
        no_of_pages = self.cleaned_data['no_of_pages']
        if no_of_pages <= 0:
            raise forms.ValidationError("No of pages must be greater than 0")
        return no_of_pages

    def clean_price(self):
        price = self.cleaned_data['price']
        if price <= 0:
            raise forms.ValidationError("Price must be greater than 0")
        return price
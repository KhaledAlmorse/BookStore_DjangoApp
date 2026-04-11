from django import forms

from authors.models import Author


class AuthorModelForm(forms.ModelForm):
    GENDER_CHOICES = [
        ("male", "Male"),
        ("female", "Female"),
    ]
    gender = forms.ChoiceField(choices=GENDER_CHOICES)

    class Meta:
        model = Author
        fields = ["name", "email", "bio", "gender"]

    def clean_name(self):
        name = self.cleaned_data["name"]
        if len(name.strip()) < 3:
            raise forms.ValidationError("Name must be at least 3 characters.")
        return name

    def clean_email(self):
        email = (self.cleaned_data.get("email") or "").strip().lower()
        qs = Author.objects.filter(email=email)
        if self.instance and self.instance.pk:
            qs = qs.exclude(pk=self.instance.pk)
        if qs.exists():
            raise forms.ValidationError("This email is already used by another author.")
        return email

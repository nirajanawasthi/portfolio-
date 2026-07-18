from django import forms
from .models import ContactMessage


class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactMessage
        fields = ["name", "email", "message"]
        widgets = {
            "name": forms.TextInput(
                attrs={"class": "form-input", "placeholder": "Your Name"}
            ),
            "email": forms.EmailInput(
                attrs={"class": "form-input", "placeholder": "your@email.com"}
            ),
            "message": forms.Textarea(
                attrs={"class": "form-input", "rows": 5, "placeholder": "Your message"}
            ),
        }

from django import forms


class ContactForm(forms.Form):
    from_email = forms.EmailField(
        required=True, label="From email", widget=forms.TextInput(attrs={"placeholder": "From Email"})
    )
    subject = forms.CharField(required=True, label="Subject", widget=forms.TextInput(attrs={"placeholder": "Subject"}))
    message = forms.CharField(widget=forms.Textarea, required=True, label="Message")

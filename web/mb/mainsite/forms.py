from django import forms


class ContactForm(forms.Form):
    from_email = forms.EmailField(required=True, label="From email")
    subject = forms.CharField(required=True, label="Subject")
    message = forms.CharField(widget=forms.Textarea, required=True, label="Message")

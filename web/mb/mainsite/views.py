from django.core.mail import BadHeaderError, send_mail
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.views.generic import TemplateView

from .forms import ContactForm


class HomeView(TemplateView):
    template_name = "home.html"

    def get(self, request):
        form = ContactForm()
        return render(request, self.template_name, {"form": form})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            subject = form.cleaned_data["subject"]
            from_email = form.cleaned_data["from_email"]
            message = form.cleaned_data["message"]
            try:
                send_mail(subject, message, from_email, ["arcimavic@gmail.com"])
            except BadHeaderError:
                return HttpResponse("Invalid header found.")
            return redirect("success")

        return render(request, self.template_name, {"form": form})


class PortfolioView(HomeView):
    template_name = "portfolio.html"


class AboutView(HomeView):
    template_name = "about.html"

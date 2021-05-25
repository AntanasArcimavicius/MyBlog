from django.core.mail import send_mail
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.views.generic import TemplateView

from .forms import ContactForm
from .models import Resume


class HomeView(TemplateView):
    template_name = "home.html"

    def get(self, request):
        form = ContactForm()
        return render(request, self.template_name, {"form": form})

    def post(self, request):
        form = ContactForm(request.POST)
        print(form.errors)
        if form.is_valid():
            subject = form.cleaned_data["subject"]
            from_email = form.cleaned_data["from_email"]
            message = form.cleaned_data["message"]
            send_mail(f'{subject} from {from_email}', message, from_email, ["arcimavic@gmail.com"])
            messages.success(request, "Message sent successfully",)

            return HttpResponseRedirect(reverse("mainsite:home",))

        return render(request, self.template_name, {"form": form})    


class PortfolioView(HomeView):
    template_name = "portfolio.html"


class AboutView(HomeView):
    template_name = "about.html"

    def get(self, request):
        form = ContactForm()
        resume = Resume.objects.first()
        return render(request, self.template_name, {"resume": resume, "form": form})

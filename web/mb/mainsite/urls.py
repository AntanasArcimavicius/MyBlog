from django.urls import path

from .views import AboutView, HomeView, PortfolioView

app_name = "mainsite"
urlpatterns = [
    path("", HomeView.as_view(), name="home"),
    path("portfolio", PortfolioView.as_view(), name="portfolio"),
    path("about", AboutView.as_view(), name="about"),
]

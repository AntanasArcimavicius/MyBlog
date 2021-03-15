from django.urls import path

from mainsite.views import HomeView

urlpatterns = [
    path("", HomeView.as_view(), name="maintenance_view"),
]

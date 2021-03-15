from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from mainsite.views import HomeView

urlpatterns = [
    path("", HomeView.as_view(), name="maintenance_view"),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

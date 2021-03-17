from django.contrib.admin import SimpleListFilter

from mb.user.models import User


class RegularUserSeeOwnItemsOnlyMixin:
    user_field = "user"

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(user=request.user)

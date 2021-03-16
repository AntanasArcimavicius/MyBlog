from django.contrib import messages
from django.templatetags.static import static
from django.urls import reverse
from jinja2 import Environment
from mb import settings


def environment(**options):
    env = Environment(**options)  # nosec
    env.globals.update(
        {
            "static": static,
            "reverse": reverse,
            "get_messages": messages.get_messages,
        }
    )
    return env

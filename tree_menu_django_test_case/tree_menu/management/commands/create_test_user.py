from typing import Any
from django.contrib.auth import get_user_model
from django.core.management import BaseCommand
from django.conf import settings


class Command(BaseCommand):
    __user_model = get_user_model()

    def handle(self, *args: Any, **options: Any) -> str | None:
        self.__user_model.objects.create_superuser(
            username=settings.ADMIN_LOGIN, password=settings.ADMIN_PASSWORD, email=None
        )

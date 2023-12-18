from enum import Enum

from django.contrib.auth.models import AbstractUser
from django.db import models


class IdentityType(Enum):
    EMPLOYEE = "Employee"
    NOTEMPLOYEE = "NotEmployee"


class User(AbstractUser):
    # extend default user to support employee status.

    status = models.CharField(
        max_length=18,
        blank=True,
        choices=[(tag.name, tag.value) for tag in IdentityType],
        default=IdentityType.NOTEMPLOYEE.value,
    )

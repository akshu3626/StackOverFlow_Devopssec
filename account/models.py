from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


class User(AbstractUser):
    is_developer = "Developer"
    is_user = "User"
    
    ROLE = [
        (is_developer, "Developer"),
        (is_user, "User"),
    ]
    role = models.CharField(
        max_length=50,
        choices=ROLE,
        default=False,
    )
    
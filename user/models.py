from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser


class User(AbstractBaseUser):
    email = models.EmailField(unique=True, verbose_name="email_address", max_length=150)
    first_name = models.CharField(max_length=100, null=True)
    last_name = models.CharField(max_length=100, null=True)
    active = models.BooleanField(default=False)
    staff = models.BooleanField(default=False)
    superuser = models.BooleanField(default=False)

    USERNAME_FIELD = "email"

    REQUIRED_FIELDS = []  # EMAIL AND PASSWORD ARE SET BY DEFAULT

    def __str__(self):
        return self.email

    def get_short_name(self):
        return self.last_name

    def get_full_name(self):
        return self.first_name + self.last_name

    def has_perm(self, perm, obj=None):
        return True  # will be doing it later

    def has_module_perm(self, app_label):
        return True  # will be doing it later

    @property
    def is_staff(self):
        return self.staff

    @property
    def is_superuser(self):
        return self.superuser

from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser


class UserManager(BaseUserManager):

    def create_user(self, email, password=None, first_name=None, last_name=None, save=True):
        if not password:
            raise ValueError("User should always have a password")

        email = self.normalize_email(email)
        user = self.model(
            email=email
        )

        user.set_password(password)
        user.first_name = first_name or str(email).split("@")[0]
        user.last_name = last_name or str(email).split("@")[0]

        if save:
            user.save(using=self._db)

        return user

    def create_superuser(self, email, password=None):
        user = self.create_user(email=email, password=password, save=False)
        user.staff = True

        user.superuser = True
        user.save(using=self._db)
        return user

    def create_staffuser(self, email, password=None):
        user = self.create_user(email=email, password=password, save=False)
        user.staff = True
        user.superuser = False
        user.save(using=self._db)
        return user


class User(AbstractBaseUser):
    email = models.EmailField(unique=True, verbose_name="email_address", max_length=150)
    first_name = models.CharField(max_length=100, null=True)
    last_name = models.CharField(max_length=100, null=True)
    active = models.BooleanField(default=True)
    staff = models.BooleanField(default=False)
    superuser = models.BooleanField(default=False)

    USERNAME_FIELD = "email"

    REQUIRED_FIELDS = []  # EMAIL AND PASSWORD ARE SET BY DEFAULT

    objects = UserManager()

    def __str__(self):
        return self.email

    def get_short_name(self):
        return self.last_name

    def get_full_name(self):
        return self.first_name + self.last_name

    def has_perm(self, perm, obj=None):
        return True  # will be doing it later

    def has_module_perms(self, app_label):
        return True  # will be doing it later

    @property
    def is_staff(self):
        return self.staff

    @property
    def is_superuser(self):
        return self.superuser

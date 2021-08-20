from django.db import models
from django.contrib.auth import get_user_model
from django.utils.text import slugify
from lib.base_model import BaseModel, random_number_gen

User = get_user_model()


class Company(BaseModel):
    user = models.OneToOneField(User, on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=150)
    description = models.TextField(null=False, blank=False)
    slug = models.SlugField()
    verified = models.BooleanField(default=False)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        slug = self.slug
        if not slug:
            self.slug = random_number_gen()
        return super().save(*args, **kwargs)


class CompanyPost(BaseModel):
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    post = models.CharField(max_length=150)
    description = models.TextField(null=False, blank=False)   
    location = models.CharField(max_length=350)
    open = models.BooleanField(default=True)
    slug = models.SlugField(default=random_number_gen)

    def __str__(self):
        return f"{self.company} --> {self.post}"

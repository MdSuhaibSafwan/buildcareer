from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import ReadOnlyPasswordHashField

User = get_user_model()


class UserAdminCreationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    password_2 = forms.CharField(widget=forms.PasswordInput, label="Confirm Password")

    class Meta:
        model = User
        fields = ["email", ]

    def clean_email(self):
        email = self.cleaned_data.get("email")
        qs = User.objects.filter(email=email)
        if qs.exists():
            raise forms.ValidationError("email is already in use")

        return email

    def clean(self):
        data = super().clean()
        ps1 = data.get("password")
        ps2 = data.get("password_2")

        if (not ps1) or (not ps2):
            raise forms.ValidationError("Both passwords should be given")

        if ps1 != ps2:
            raise forms.ValidationError("Both the passwords did not match")

        return data

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data.get("password"))
        if commit:
            user.save()
    
        return user


class UserAdminUpdateForm(forms.ModelForm):
    password = ReadOnlyPasswordHashField()

    class Meta:
        model = User
        fields = ["email", "first_name", "last_name", "staff", "superuser"]

    def clean_password(self):
        return self.initial["password"]

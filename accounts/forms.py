from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.core.exceptions import ValidationError
from django.forms.fields import EmailField
from django.forms.forms import Form


class SignUpForm(UserCreationForm):
    fname = forms.CharField(label='First name', min_length=4, max_length=150)
    lname = forms.CharField(label='Last name', min_length=4, max_length=150)
    email = forms.EmailField(label='Email')
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirm password', widget=forms.PasswordInput)

    def init(self,*args , **kwargs):
        super().init(*args , **kwargs)
        self.fields["fname"].widget.attrs.update({
            'placeholder':'First name',})
        self.fields["lname"].widget.attrs.update({
            'placeholder':'Last name',})
        self.fields["email"].widget.attrs.update({
            'placeholder':'email',})
        self.fields["password1"].widget.attrs.update({
            'placeholder':'password',})
        self.fields["password2"].widget.attrs.update({
            'placeholder':'confirm password',})
    class Meta:
        model= User
        fields=['fname', 'lname', 'email','password1','password2']

    def clean_email(self):
        email = self.cleaned_data.get("email")
        new = User.objects.filter(email=email)
        if User.objects.filter(email=email).exists() or new.count():
            raise forms.ValidationError("Email already exist")
        return email

    def clean_password2(self):
        print("pass")
        password1 = self.cleaned_data['password1']
        password2 = self.cleaned_data['password2']

        if password1 and password2 and password1 != password2:
            raise ValidationError("Password didn't match")
        return password2

    def save(self, commit=True):
        user = User.objects.create_user(
            self.cleaned_data['email'],
            self.cleaned_data['password1']
        )
        return user

class LoginForm(AuthenticationForm):
    def init(self,*args , **kwargs):
        super().init(*args , **kwargs)
        self.fields["email"].widget.attrs.update({
            'required':'',
            'name':'email',
            'id':'email',
            'type':'text',
            'class':'form-input',
            'placeholder':'email',
            'maxlenght':'30',
            'minlenght':'6'
        })

        self.fields["password"].widget.attrs.update({
            'required': '',
            'name': 'password',
            'id': 'password',
            'type': 'text',
            'class': 'form-input',
            'placeholder': 'password',
            'maxlenght': '100',
            'minlenght': '6'
        })
    class Meta:
        model= User
        fields=['email', 'password']

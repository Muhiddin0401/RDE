from django import forms
from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator
from .models import *

class RegionForm(forms.ModelForm):
    class Meta:
        model = Region
        fields = ['title']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Viloyat nomini kiriting'}),
        }

    def clean_title(self):
        title = self.cleaned_data.get('title')
        if not title[0].isupper():
            raise ValidationError("Viloyat nomining bosh harfi katta bo'lishi kerak!!!")
        if any(char.isdigit() for char in title):
            raise ValidationError("Viloyat nomida raqam bo'lmasligi kerak!!!")
        if not (3 <= len(title) <= 50):
            raise ValidationError("Viloyat nomi uzunligi 3 dan 50 ta belgigacha bo‘lishi kerak!!!")
        return title

class DepartmentForm(forms.ModelForm):
    class Meta:
        model = Department
        fields = ['title']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Tashkilot nomini kiriting'}),
        }

    def clean_title(self):
        title = self.cleaned_data.get('title')
        if not title.isupper():
            raise ValidationError("Tashkilot nomi faqat katta harflardan iborat bo‘lishi kerak!!!")
        if any(char.isdigit() for char in title):
            raise ValidationError("Tashkilot nomida raqam bo‘lishi mumkin emas!!!")
        if not (3 <= len(title) <= 50):
            raise ValidationError("Tashkilot nomi uzunligi 3 dan 50 ta belgigacha bo‘lishi kerak!!!")
        return title

class EmployeeForm(forms.ModelForm):
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email'}),
        error_messages={'invalid': "Emailni to‘g‘ri formatda kiriting!"}
    )

    phone = forms.CharField(
        validators=[RegexValidator(
            regex=r'^\+998[0-9]{9}$',
            message="Telefon raqami +998 bilan boshlanib, 9 ta raqamdan iborat bo‘lishi kerak!",
            code='invalid_phone'
        )],
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Phone'}),
    )

    class Meta:
        model = Employee
        fields = ['lastname', 'firstname', 'middlename', 'email', 'phone', 'file', 'region', 'department']
        widgets = {
            'lastname': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Familiyangiz:'}),
            'firstname': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ismingiz:'}),
            'middlename': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Sharifingiz:'}),
            'file': forms.ClearableFileInput(attrs={'class': 'form-control'}),
            'region': forms.Select(attrs={'class': 'form-control'}),
            'department': forms.Select(attrs={'class': 'form-control'}),
        }

    def clean_lastname(self):
        last = self.cleaned_data.get('lastname')
        if not last[0].isupper():
            raise ValidationError("Familiya bosh harf bilan boshlanishi kerak!")
        if any(char.isdigit() for char in last):
            raise ValidationError("Familiyaga raqam kiritish mumkin emas!")
        if not (3 <= len(last) <= 25):
            raise ValidationError("Familiya uzunligi 3 tadan 25 ta belgigacha bo‘lishi kerak!")
        return last

    def clean_firstname(self):
        first = self.cleaned_data.get('firstname')
        if not first[0].isupper():
            raise ValidationError("Ism bosh harf bilan boshlanishi kerak!")
        if any(char.isdigit() for char in first):
            raise ValidationError("Ismda raqam bo‘lishi mumkin emas!")
        if not (3 <= len(first) <= 25):
            raise ValidationError("Ism uzunligi 3 tadan 25 ta belgigacha bo‘lishi kerak!")
        return first

    def clean_middlename(self):
        middle = self.cleaned_data.get('middlename')
        if not middle[0].isupper():
            raise ValidationError("Sharif bosh harf bilan boshlanishi kerak!")
        if any(char.isdigit() for char in middle):
            raise ValidationError("Sharifda raqam bo‘lishi mumkin emas!")
        if not (3 <= len(middle) <= 25):
            raise ValidationError("Sharif uzunligi 3 tadan 25 ta belgigacha bo‘lishi kerak!")
        return middle

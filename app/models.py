from django.db import models
from django.core.validators import RegexValidator
from django.core.exceptions import ValidationError


class Base(models.Model):
    """ Abstract model barcha modellarga vorislik qiladi """
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Yaratilgan sana")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Yangilangan sana")

    class Meta:
        abstract = True

    def __str__(self):
        return f"Base Object ({self.id})"


# ✅ REGION MODELI: Nom faqat harflardan iborat va bosh harfi katta bo‘lishi kerak
def validate_region_title(value):
    if not value[0].isupper():
        raise ValidationError("Viloyat nomining bosh harfi katta bo‘lishi kerak!")
    if any(char.isdigit() for char in value):
        raise ValidationError("Viloyat nomida raqam bo‘lishi mumkin emas!")


class Region(Base):
    title = models.CharField(max_length=50, validators=[validate_region_title])

    def __str__(self):
        return self.title


def validate_department_title(value):
    if not value.isupper():
        raise ValidationError("Tashkilot nomining barcha harflari katta bo‘lishi kerak!")
    if any(char.isdigit() for char in value):
        raise ValidationError("Tashkilot nomida raqam bo‘lishi mumkin emas!")


class Department(Base):
    title = models.CharField(max_length=50, validators=[validate_department_title])

    def __str__(self):
        return self.title


def validate_name(value):
    if not value[0].isupper():
        raise ValidationError("Ism, familiya va sharifning bosh harfi katta bo‘lishi kerak!")
    if any(char.isdigit() for char in value):
        raise ValidationError("Ism, familiya va sharifda raqam bo‘lishi mumkin emas!")


def validate_file_extension(value):
    import os
    ext = os.path.splitext(value.name)[1]  # Fayl kengaytmasini olish
    valid_extensions = ['.pdf', '.doc', '.docx']
    if ext.lower() not in valid_extensions:
        raise ValidationError("Faqat PDF va DOC/DOCX fayllar yuklash mumkin!")


class Employee(Base):
    lastname = models.CharField(max_length=50, validators=[validate_name])
    firstname = models.CharField(max_length=50, validators=[validate_name])
    middlename = models.CharField(max_length=50, validators=[validate_name])

    email = models.EmailField(unique=True)

    phone = models.CharField(
        max_length=13, blank=True, null=True,
        validators=[RegexValidator(regex=r'^\+998[0-9]{9}$',
                                   message="Telefon raqami +998 bilan boshlanishi va 9 ta raqam bo‘lishi kerak!")]
    )

    file = models.FileField(upload_to='files/', validators=[validate_file_extension], null=True, blank=True)

    region = models.ForeignKey(Region, on_delete=models.CASCADE, null=True, blank=True)
    department = models.ForeignKey(Department, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return f"{self.lastname} {self.firstname}"

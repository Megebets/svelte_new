from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin

class CustomUserManager(BaseUserManager):
    def create_user(self, phone_number, password=None, **extra_fields):
        if not phone_number:
            raise ValueError('Phone number must be set')
        user = self.model(phone_number=phone_number, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, phone_number, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self.create_user(phone_number, password, **extra_fields)

class CustomUser(AbstractBaseUser, PermissionsMixin):
    phone_number = models.CharField(max_length=15, unique=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = CustomUserManager()

    USERNAME_FIELD = 'phone_number'  # Используем phone_number вместо username
    REQUIRED_FIELDS = []  # Ничего дополнительного не требуется

    def __str__(self):
        return self.phone_number

class Profile(models.Model):
    user = models.OneToOneField('CustomUser', on_delete=models.CASCADE, related_name='profile')  # Исправлено на CustomUser
    avatar = models.ImageField(upload_to='avatars/', blank=True, null=True)
    last_name = models.CharField(max_length=100, blank=True)
    name = models.CharField(max_length=100, blank=True)
    nationality = models.CharField(max_length=100, blank=True)
    middle_name = models.CharField(max_length=100, blank=True)
    pol = models.CharField(max_length=10, blank=True)
    has_parents = models.BooleanField(default=False)
    livingplace = models.CharField(max_length=255, blank=True)
    birthdate = models.DateField(null=True, blank=True)
    birthplace = models.CharField(max_length=255, blank=True)
    residence = models.CharField(max_length=255, blank=True)
    contact_phone = models.CharField(max_length=20, blank=True)
    trusted_person_phone = models.CharField(max_length=20, blank=True)
    education = models.BooleanField(default=False)
    education_level = models.CharField(max_length=100, blank=True)
    specialty = models.CharField(max_length=100, blank=True)
    has_working = models.BooleanField(default=False)
    has_housing = models.BooleanField(default=False)
    was_married = models.BooleanField(default=False)
    has_children = models.BooleanField(default=False)
    children_boys = models.CharField(max_length=10, blank=True)
    children_girls = models.CharField(max_length=10, blank=True)
    children_ages = models.CharField(max_length=255, blank=True)
    height = models.IntegerField(default=170)
    has_criminal_record = models.BooleanField(default=False)
    has_bad_habits = models.CharField(max_length=100, blank=True)
    performs_namaz = models.BooleanField(default=False)
    clothing_preference = models.CharField(max_length=100, blank=True)
    spouse_nationality_importance = models.BooleanField(default=False)
    spouse_age_preference = models.IntegerField(default=30)
    ok_with_divorced_spouse = models.BooleanField(default=False)
    ok_with_spouse_children = models.BooleanField(default=False)
    clothing_preferences = models.TextField(blank=True)
    health = models.TextField(blank=True)
    willing_to_relocate = models.BooleanField(default=False)
    agree_to_be_second_wife = models.BooleanField(default=False)
    plan_to_have_children = models.BooleanField(default=True)
    health_status = models.TextField(blank=True)
    additional_info = models.TextField(blank=True)
    spouse_age = models.CharField(max_length=10, blank=True)
    spouse_requirements = models.TextField(blank=True)
    profile_completion_date = models.DateTimeField(null=True, blank=True)
    consent_to_data_processing = models.BooleanField(default=False)
    madhhab = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return f"Profile of {self.user.phone_number}"
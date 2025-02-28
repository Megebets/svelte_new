from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager
from datetime import datetime

class CustomUserManager(BaseUserManager):
    def create_user(self, phone_number, password=None, **extra_fields):
        if not phone_number:
            raise ValueError('Phone number is required')
        user = self.model(phone_number=phone_number, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, phone_number, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')
        return self.create_user(phone_number, password, **extra_fields)

class CustomUser(AbstractUser):
    username = None
    phone_number = models.CharField(max_length=15, unique=True)
    USERNAME_FIELD = 'phone_number'
    REQUIRED_FIELDS = []
    objects = CustomUserManager()

class Profile(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to='avatars/', blank=True, null=True)
    last_name = models.CharField(max_length=100, blank=True)
    name = models.CharField(max_length=100, blank=True)
    nationality = models.CharField(max_length=100, blank=True)
    middle_name = models.CharField(max_length=100, blank=True)
    pol = models.CharField(max_length=10, blank=True)
    has_parents = models.BooleanField(default=False)
    livingplace = models.BooleanField(default=False)
    birthdate = models.DateField(blank=True, null=True)
    birthplace = models.CharField(max_length=200, blank=True)
    residence = models.CharField(max_length=200, blank=True)
    contact_phone = models.CharField(max_length=15, blank=True)
    trusted_person_phone = models.CharField(max_length=15, blank=True)
    education = models.BooleanField(default=False)
    education_level = models.CharField(max_length=100, blank=True)
    specialty = models.CharField(max_length=100, blank=True)
    has_working = models.BooleanField(default=False)
    has_housing = models.BooleanField(default=False)
    was_married = models.BooleanField(default=False)
    has_children = models.BooleanField(default=False)
    children_boys = models.IntegerField(default=0)
    children_girls = models.IntegerField(default=0)
    children_ages = models.CharField(max_length=100, blank=True)
    height = models.IntegerField(default=170)
    has_criminal_record = models.BooleanField(default=False)
    has_bad_habits = models.CharField(max_length=200, blank=True)
    performs_namaz = models.BooleanField(default=False)
    clothing_preference = models.CharField(max_length=200, blank=True)
    spouse_nationality_importance = models.BooleanField(default=False)
    spouse_age_min = models.IntegerField(default=18)
    spouse_age_max = models.IntegerField(default=30)
    ok_with_divorced_spouse = models.BooleanField(default=False)
    ok_with_spouse_children = models.BooleanField(default=False)
    clothing_preferences = models.CharField(max_length=200, blank=True)
    health = models.CharField(max_length=200, blank=True)
    willing_to_relocate = models.BooleanField(default=False)
    agree_to_be_second_wife = models.BooleanField(default=False)
    plan_to_have_children = models.BooleanField(default=True)
    health_status = models.CharField(max_length=200, blank=True)
    additional_info = models.TextField(blank=True)
    spouse_requirements = models.TextField(blank=True)
    profile_completion_date = models.DateTimeField(auto_now=True)
    consent_to_data_processing = models.BooleanField(default=False)
    madhhab = models.CharField(max_length=100, blank=True)
    is_approved = models.BooleanField(default=False)

    def get_age(self):
        if self.birthdate:
            today = datetime.now().date()
            return today.year - self.birthdate.year - ((today.month, today.day) < (self.birthdate.month, self.birthdate.day))
        return None

class Tip(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
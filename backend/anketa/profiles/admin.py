from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser, Profile, Tip

# Регистрация CustomUser с кастомным админом
@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ('phone_number', 'is_staff', 'is_superuser', 'is_active')
    list_filter = ('is_staff', 'is_superuser', 'is_active')
    fieldsets = (
        (None, {'fields': ('phone_number', 'password')}),
        ('Personal info', {'fields': ()}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('phone_number', 'password1', 'password2', 'is_staff', 'is_superuser'),
        }),
    )
    search_fields = ('phone_number',)
    ordering = ('phone_number',)

# Регистрация Profile
@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'name', 'pol', 'is_approved')
    list_filter = ('pol', 'is_approved')
    search_fields = ('name', 'user__phone_number')
    fieldsets = (
        (None, {'fields': ('user', 'is_approved')}),
        ('Personal Info', {'fields': ('name', 'last_name', 'middle_name', 'nationality', 'pol', 'birthdate', 'birthplace', 'residence')}),
        ('Contact Info', {'fields': ('contact_phone', 'trusted_person_phone')}),
        ('Family', {'fields': ('has_parents', 'livingplace', 'has_children', 'children_boys', 'children_girls', 'children_ages')}),
        ('Other', {'fields': ('height', 'education', 'education_level', 'specialty', 'has_working', 'has_housing', 'was_married', 'has_criminal_record', 'performs_namaz', 'madhhab', 'has_bad_habits', 'willing_to_relocate', 'plan_to_have_children', 'clothing_preferences', 'health', 'additional_info', 'spouse_requirements')}),
        ('Spouse Preferences', {'fields': ('spouse_age_min', 'spouse_age_max', 'ok_with_divorced_spouse', 'ok_with_spouse_children', 'spouse_nationality_importance')}),
        ('Consent', {'fields': ('consent_to_data_processing',)}),
    )

# Регистрация Tip
@admin.register(Tip)
class TipAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at')
    search_fields = ('title', 'description')
    list_filter = ('created_at',)
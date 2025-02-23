from rest_framework import serializers
from .models import CustomUser, Profile

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['phone_number']

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = [
            'avatar', 'last_name', 'name', 'nationality', 'middle_name', 'pol', 'has_parents', 
            'livingplace', 'birthdate', 'birthplace', 'residence', 'contact_phone', 
            'trusted_person_phone', 'education', 'education_level', 'specialty', 'has_working', 
            'has_housing', 'was_married', 'has_children', 'children_boys', 'children_girls', 
            'children_ages', 'height', 'has_criminal_record', 'has_bad_habits', 'performs_namaz', 
            'clothing_preference', 'spouse_nationality_importance', 'spouse_age_preference', 
            'ok_with_divorced_spouse', 'ok_with_spouse_children', 'clothing_preferences', 
            'health', 'willing_to_relocate', 'agree_to_be_second_wife', 'plan_to_have_children', 
            'health_status', 'additional_info', 'spouse_age', 'spouse_requirements', 
            'profile_completion_date', 'consent_to_data_processing', 'madhhab'
        ]
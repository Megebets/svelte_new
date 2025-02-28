from rest_framework import serializers
from .models import CustomUser, Profile, Tip
from datetime import datetime

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['phone_number']

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = '__all__'

class OtherProfileSerializer(serializers.ModelSerializer):
    age = serializers.SerializerMethodField()

    class Meta:
        model = Profile
        fields = [
            'name', 'age', 'nationality', 'residence', 'height', 'has_children',
            'education', 'has_housing', 'has_parents', 'livingplace', 'was_married',
            'has_criminal_record', 'performs_namaz', 'madhhab', 'has_bad_habits',
            'willing_to_relocate', 'plan_to_have_children', 'clothing_preferences',
            'health', 'additional_info', 'spouse_requirements'
        ]

    def get_age(self, obj):
        return obj.get_age()

class TipSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tip
        fields = ['title', 'description']
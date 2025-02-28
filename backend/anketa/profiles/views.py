from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken
from .models import CustomUser, Profile, Tip
from .serializers import UserSerializer, ProfileSerializer, OtherProfileSerializer, TipSerializer
from django.utils import timezone
import logging

logger = logging.getLogger(__name__)

@api_view(['POST'])
def register_view(request):
    phone_number = request.data.get('phone_number')
    password = request.data.get('password')
    if not phone_number or not password:
        return Response({'error': 'Phone number and password are required'}, status=400)
    if CustomUser.objects.filter(phone_number=phone_number).exists():
        return Response({'error': 'User already exists'}, status=400)
    user = CustomUser.objects.create_user(phone_number=phone_number, password=password)
    Profile.objects.create(user=user)
    refresh = RefreshToken.for_user(user)
    return Response({
        'refresh': str(refresh),
        'access': str(refresh.access_token)
    }, status=201)

@api_view(['GET', 'PUT'])
@permission_classes([IsAuthenticated])
def profile_view(request):
    try:
        profile, created = Profile.objects.get_or_create(user=request.user)
        if request.method == 'GET':
            serializer = ProfileSerializer(profile)
            logger.info(f"Profile retrieved for user {request.user.phone_number}: {serializer.data}")
            return Response(serializer.data)
        elif request.method == 'PUT':
            serializer = ProfileSerializer(profile, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                logger.info(f"Profile updated for user {request.user.phone_number}: {serializer.data}")
                return Response(serializer.data)
            logger.error(f"Profile update failed: {serializer.errors}")
            return Response(serializer.errors, status=400)
    except Exception as e:
        logger.error(f"Error in profile_view: {str(e)}")
        return Response({'error': str(e)}, status=500)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def tips_view(request):
    tips = Tip.objects.all()
    serializer = TipSerializer(tips, many=True)
    return Response(serializer.data)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def other_profiles_view(request):
    if not request.user.profile.is_approved:
        return Response({'error': 'Your profile is not approved yet'}, status=403)

    current_profile = request.user.profile
    opposite_gender = 'Женский' if current_profile.pol == 'Мужской' else 'Мужской'

    profiles = Profile.objects.filter(
        is_approved=True,
        pol=opposite_gender
    ).exclude(user=request.user)

    if not current_profile.ok_with_divorced_spouse:
        profiles = profiles.filter(was_married=False)
    if not current_profile.ok_with_spouse_children:
        profiles = profiles.filter(has_children=False)

    current_year = timezone.now().year
    min_birth_year = current_year - current_profile.spouse_age_max
    max_birth_year = current_year - current_profile.spouse_age_min
    profiles = profiles.filter(
        birthdate__year__gte=min_birth_year,
        birthdate__year__lte=max_birth_year
    ).order_by('-profile_completion_date')

    serializer = OtherProfileSerializer(profiles, many=True)
    return Response(serializer.data)
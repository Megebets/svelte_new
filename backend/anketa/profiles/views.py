from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from .models import CustomUser, Profile
from .serializers import ProfileSerializer

@api_view(['POST'])
@permission_classes([AllowAny])
def register_view(request):
    phone_number = request.data.get('phone_number')
    password = request.data.get('password')
    if not phone_number or not password:
        return Response({'error': 'Phone number and password are required'}, status=400)
    if CustomUser.objects.filter(phone_number=phone_number).exists():
        return Response({'error': 'Phone number already registered'}, status=400)
    user = CustomUser.objects.create_user(phone_number=phone_number, password=password)
    Profile.objects.create(user=user)
    
    refresh = RefreshToken.for_user(user)
    return Response({
        'refresh': str(refresh),
        'access': str(refresh.access_token),
        'message': 'User registered successfully'
    }, status=201)

# Другие обработчики
@api_view(['GET', 'PUT'])
@permission_classes([IsAuthenticated])
def profile_view(request):
    profile, created = Profile.objects.get_or_create(user=request.user)
    if request.method == 'GET':
        serializer = ProfileSerializer(profile)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = ProfileSerializer(profile, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

@api_view(['GET'])
@permission_classes([AllowAny])
def archive_view(request):
    return Response({'message': 'This is the public archive'})

@api_view(['GET'])
@permission_classes([AllowAny])
def home_view(request):
    return Response({'message': 'Welcome to the home page'})

@api_view(['GET'])
@permission_classes([AllowAny])
def about_view(request):
    return Response({'message': 'About us'})
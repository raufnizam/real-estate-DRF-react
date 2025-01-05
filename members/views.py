from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.decorators import api_view, permission_classes

from api.models import Property
from api.serializers import PropertySerializer, UserSerializer


class RegisterView(APIView):

    permission_classes = [AllowAny]

    def post(self, request, *args, **kwargs):
        username = request.data.get('username')
        email = request.data.get('email')
        password = request.data.get('password')

        if not username or not email or not password:
            return Response(
                {"error": "Username, email, and password are required."},
                status=status.HTTP_400_BAD_REQUEST,
            )

        if User.objects.filter(username=username).exists():
            return Response(
                {"error": "A user with this username already exists."},
                status=status.HTTP_400_BAD_REQUEST,
            )

        if User.objects.filter(email=email).exists():
            return Response(
                {"error": "A user with this email already exists."},
                status=status.HTTP_400_BAD_REQUEST,
            )

        user = User.objects.create(
            username=username,
            email=email,
            password=make_password(password),
        )

        refresh = RefreshToken.for_user(user)

        return Response(
            {
                "message": "User created successfully.",
                "refresh": str(refresh),
                "access": str(refresh.access_token),
            },
            status=status.HTTP_201_CREATED,
        )




class UserDashboardView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        user = request.user  

        user_data = UserSerializer(user).data

        user_properties = Property.objects.filter(author=user)
        properties_data = PropertySerializer(user_properties, many=True).data

        return Response(
            {
                "user_info": user_data,
                "user_properties": properties_data,
            },
            status=200
        )



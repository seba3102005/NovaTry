from django.shortcuts import render
from .serializers import RegisterSerializer,LoginSerializer,LogoutSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.permissions import IsAuthenticated
# Create your views here.


class RegisterView(APIView):
    
    def post(self,request):
        serializer = RegisterSerializer(data = request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({"message":"user is created successfully"},status=status.HTTP_200_OK)


class LoginView(APIView):
    def post(self,request):
        serializer =  LoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        username = serializer.validated_data.get('username').strip()
        password = serializer.validated_data.get('password').strip()


        user = authenticate(username=username,password=password)

        if not user:
            return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)
        
        refresh = RefreshToken.for_user(user)
        return Response({"user":{"id":user.id,"username":user.username,"email":user.email},"refresh":str(refresh),"access":str(refresh.access_token)},status=status.HTTP_200_OK)


class LogoutView(APIView):
    permission_classes = [IsAuthenticated]
    def post(self,request):
        serializer = LogoutSerializer(data = request.data)
        serializer.is_valid(raise_exception=True)

        refresh = serializer.validated_data.get('refresh').strip()
        token = RefreshToken(refresh)

        try:
            token.blacklist()
            return Response({'message':'logged out successfully'},status=status.HTTP_200_OK)
            
        except:
            return Response({'message':'error happend while logging out'},status=status.HTTP_400_BAD_REQUEST)




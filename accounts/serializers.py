from rest_framework import serializers
from django.contrib.auth import get_user_model

User = get_user_model()

class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username','password','email']
        extra_kwargs = {
            'email':{'required':True}
        }

    def create(self,validated_data):
        password = validated_data.pop('password')
        user = User(**validated_data)
        user.set_password(password)
        user.save()
        return user

    
class LoginSerializer(serializers.Serializer): 
    username = serializers.CharField(max_length = 150)
    password = serializers.CharField(min_length = 4)


class LogoutSerializer(serializers.Serializer):
    refresh = serializers.CharField()

    
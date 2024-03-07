from rest_framework import serializers
from .models import StudentModel
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model= User
        fields=['username','first_name','last_name','email']
        # fields='__all__'
        


class StudentSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    class Meta:
        model = StudentModel
        fields='__all__'
        depth=1


class SignUpSerializer(serializers.Serializer):
    username = serializers.CharField()
    email = serializers.EmailField()
    password = serializers.CharField()
    
    def validate(self, data):
        if data['username']:
            if User.objects.filter(username= data['username']).exists():
                raise serializers.ValidationError("Username already exists")  
        if data['email']:
            if User.objects.filter(email= data['email']).exists():
                raise serializers.ValidationError("Email already exists")
        return data
    
    def create(self, validated_data):
        user = User.objects.create(username=validated_data['username'],email=validated_data['email'])
        user.set_password(validated_data['password'])
        user.save()
        student = StudentModel.objects.create(user=user)
        student.save()
        return validated_data
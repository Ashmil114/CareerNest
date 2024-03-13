from rest_framework import serializers
from .models import StudentModel
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model= User
        fields=['username','first_name','last_name','email']


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentModel
        fields='__all__'
        depth=1
    
    def update(self, instance, validated_data):
        user_data = validated_data.pop('user', {})
        instance.department = validated_data.get('department', instance.department)
        instance.phone = validated_data.get('phone', instance.phone)
        instance.ten_certificate = validated_data.get('ten_certificate', instance.ten_certificate)
        instance.plustwo_certificate = validated_data.get('plustwo_certificate', instance.plustwo_certificate)
        instance.degree_certificate = validated_data.get('degree_certificate', instance.degree_certificate)
        instance.resume = validated_data.get('resume', instance.resume)
        instance.skills = validated_data.get('skills', instance.skills)
        instance.image = validated_data.get('image', instance.image)

        if user_data:
            user_instance, created = User.objects.get_or_create(username=user_data.get('username'))
            user_serializer = UserSerializer(user_instance, data=user_data)
            if user_serializer.is_valid():
                user_serializer.save()
            else:
                raise serializers.ValidationError(user_serializer.errors)
            instance.user = user_instance

        instance.save()
        return instance
    

    
    

class SignUpSerializer(serializers.Serializer):
    first_name = serializers.CharField()
    last_name = serializers.CharField()
    username = serializers.CharField()
    email = serializers.EmailField()
    password = serializers.CharField()
    
    
    def validate(self, data):
        if data['username']:
            if User.objects.filter(username = data['username']).exists():
                raise serializers.ValidationError("Username already exists")  
        if data['email']:
            if User.objects.filter(email = data['email']).exists():
                raise serializers.ValidationError("Email already exists")
        return data
    
    def create(self, validated_data):
        user = User.objects.create(username=validated_data['username'],email=validated_data['email'],first_name=validated_data['first_name'],last_name=validated_data['last_name'])
        user.set_password(validated_data['password'])
        user.save()
        student = StudentModel.objects.create(user=user)
        student.save()
        return validated_data
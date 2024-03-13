from rest_framework import serializers
from .models import JobsModel,ApplyedJobModel,CompanyModel,SaveJobModel
from django.contrib.auth.models import User



class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = CompanyModel
        fields='__all__'
        depth=1

class JobsSerializer(serializers.ModelSerializer):
    class Meta:
        model = JobsModel
        fields = '__all__'
        depth = 2
    
    def update(self, instance, validated_data):
        return super().update(instance, validated_data)

class ApplyJobListSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplyedJobModel
        fields = '__all__'
        depth = 2
 
 
class SaveJobListSerializer(serializers.ModelSerializer):
    class Meta:
        model = SaveJobModel
        fields = '__all__'
        depth = 2   

class CompanySignUpSerializer(serializers.Serializer):
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
        user = User.objects.create(username=validated_data['username'],email=validated_data['email'])
        user.set_password(validated_data['password'])
        user.save()
        company = CompanyModel.objects.create(company=user)
        company.save()
        return validated_data
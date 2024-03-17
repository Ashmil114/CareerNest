from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework import status

# Models
from .models import StudentModel

# Serializers
from .serializer import StudentSerializer,SignUpSerializer


class StudentsView(APIView):
    permission_classes=[IsAuthenticated]
    authentication_classes=[TokenAuthentication]
    
    
    def get(self,request):
        obj = StudentModel.objects.all()
        serializerdata = StudentSerializer(obj,many=True)
        return Response(serializerdata.data)
    
    
    
    
    
class StudentDataView(APIView):
    def get_object(self, pk):
        try:
            return StudentModel.objects.get(pk=pk)
        except StudentModel.DoesNotExist:
            raise Response({'message':'Not Found'})
    
    def get(self, request, pk, format=None):
        _data = self.get_object(pk)
        serializer = StudentSerializer(_data)
        return Response(serializer.data)

        
    
    def put(self, request, pk, format=None):
        obj = self.get_object(pk)
        serializer = StudentSerializer(obj, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
   
    
    
class SignUpView(APIView):
    
    def post(self,request):
        _data = request.data
        serializer=SignUpSerializer(data = _data)
        if not serializer.is_valid():
            return Response(serializer.errors)
        serializer.save()
        return Response({'message':'User Created'})
    
    
        

class CustomAuthToken(ObtainAuthToken):

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data,
                                           context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        return Response({
            'token': token.key,
            'user_id': user.pk,
            'email': user.email,
            'username':user.username
        })
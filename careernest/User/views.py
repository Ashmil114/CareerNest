from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication

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
    
    
class SignUpView(APIView):
    
    def post(self,request):
        _data = request.data
        serializer=SignUpSerializer(data = _data)
        if not serializer.is_valid():
            return Response(serializer.errors)
        serializer.save()
        return Response({'message':'User Created'})
        


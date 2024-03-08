from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView

#Models
from .models import JobsModel
# Serializer
from .serializer import JobsSerializer

class JobsView(APIView):
    def get(self,request):
        jobs = JobsModel.objects.all()
        serializer = JobsSerializer(jobs,many=True)
        return Response(serializer.data)
    
    def post(self,request):
        _data = request.data
        serializer_data = JobsSerializer(data=_data)
        
        if not serializer_data.is_valid():
            return Response(serializer_data.errors)
        
        serializer_data.save()
        return Response(serializer_data.data)
    
    def put(self, request, pk, format=None):
        job = JobsModel.objects.get(pk=pk)
        serializer = JobsSerializer(job, data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors)
        serializer.save()
        return Response(serializer.data)
    
class JobView(APIView):
    
    def get(self, request, pk, format=None):
        _data = JobsModel.objects.get(pk=pk)
        serializer = JobsSerializer(_data)
        return Response(serializer.data)
    
    def put(self, request, pk, format=None):
        job = JobsModel.objects.get(pk=pk)
        serializer = JobsSerializer(job, data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors)
        serializer.save()
        return Response(serializer.data)
    
    

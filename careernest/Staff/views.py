from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView

#Models
from .models import JobsModel,ApplyedJobModel
from User.models import StudentModel
# Serializer
from .serializer import JobsSerializer,ApplyJobListSerializer

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
    
    
class ApplyJobView(APIView):
    
    
    
    def get(self,request):
        applyJob = ApplyedJobModel.objects.all()
        serializer = ApplyJobListSerializer(applyJob,many=True)
        return Response(serializer.data)
    
    def post(self,request):
        user_id = request.data.get('user_id')
        job_id = request.data.get('job_id')

        if not user_id or not job_id:
            return Response({'error': 'user_id and job_id are required'})

        try:
            user = StudentModel.objects.get(pk=user_id)
            job = JobsModel.objects.get(pk=job_id)
        except (StudentModel.DoesNotExist, JobsModel.DoesNotExist):
            return Response({'error': 'User or Job not found'})

        already_apply = ApplyedJobModel.objects.filter(job__id = job_id , user__id = user_id)
        
        if not already_apply:
            applyJob = ApplyedJobModel.objects.create(user=user, job=job, status='pending')
            applyJob.save()
            return Response({'message':"Applyed"})
        else:
            return Response({'message':"Your Already Applyed"})
        
        
        

        
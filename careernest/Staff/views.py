from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication

#Models
from .models import JobsModel,ApplyedJobModel,CompanyModel,SaveJobModel
from User.models import StudentModel
# Serializer
from .serializer import JobsSerializer,ApplyJobListSerializer,CompanySignUpSerializer,CompanySerializer,SaveJobListSerializer


class CompanyView(APIView):
    permission_classes=[IsAuthenticated]
    authentication_classes=[TokenAuthentication]
    
    def get(self,request):
        obj = CompanyModel.objects.all()
        serializerdata = CompanySerializer(obj,many=True)
        return Response(serializerdata.data)

class JobsView(APIView):
    permission_classes=[IsAuthenticated]
    authentication_classes=[TokenAuthentication]
    
    def get(self,request):
        jobs = JobsModel.objects.all()
        serializer = JobsSerializer(jobs,many=True)
        return Response(serializer.data)
    
    def post(self,request):
        _data = request.data
        
        company = CompanyModel.objects.get(pk=_data.get('companyid'))
        image  =_data.get('image')
        title =_data.get('title')
        type =_data.get('type')
        vaccancies =_data.get('vaccancies')
        package  =_data.get('package')
        experiance =_data.get('experiance')
        description =_data.get('description')
        qualifications =_data.get('qualifications')
        responsibility =_data.get('responsibility')
        # skills=_data.get('skills')
        
        Already_Added=JobsModel.objects.filter(title=title,company=company)
        if not Already_Added:
            Jobs= JobsModel.objects.create(image=image,title=title,type=type,vaccancies=vaccancies,package=package,experiance=experiance,description=description,qualifications=qualifications,responsibility=responsibility,company=company)
            print(Jobs)
            return Response("Job Added")
        else:
            return Response("Job Already Added")
    
    
class JobView(APIView):
    permission_classes=[IsAuthenticated]
    authentication_classes=[TokenAuthentication]
    
    
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
    permission_classes=[IsAuthenticated]
    authentication_classes=[TokenAuthentication]
    
    
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
        
    

class CompanySignUpView(APIView):
    
    def post(self,request):
        _data = request.data
        serializer=CompanySignUpSerializer(data = _data)
        if not serializer.is_valid():
            return Response(serializer.errors)
        serializer.save()
        return Response({'message':'User Created'})
    


class SaveJobView(APIView):
    permission_classes=[IsAuthenticated]
    authentication_classes=[TokenAuthentication]
    
    
    def get(self,request):
        saveJob = SaveJobModel.objects.all()
        serializer = SaveJobListSerializer(saveJob,many=True)
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

        already_save = SaveJobModel.objects.filter(job__id = job_id , user__id = user_id)
        
        if not already_save:
            saveJob = SaveJobModel.objects.create(user=user, job=job)
            saveJob.save()
            return Response({'message':"Saved"})
        else:
            return Response({'message':"Your Already Saved"})
        
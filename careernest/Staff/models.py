from django.db import models
from User.models import StudentModel

# Create your models here.

JOB_TYPE = (
    ("remote","remote"),
    ("parttime","parttime"),
    ("office","office"),
)

class JobsModel(models.Model):
    title = models.CharField(max_length=255)
    company = models.CharField(max_length=255)
    type = models.CharField(choices=JOB_TYPE,max_length=100)
    vaccancies = models.IntegerField()
    package = models.CharField(max_length=100)
    experiance = models.FloatField(default=0)
    requirements = models.TextField(max_length=500)
    
    def __str__(self) -> str:
        return self.title
    
JOB_STATUS = (
    ("pending","pending"),
    ("approved","approved"),
    ("rejected","rejected")
)

class ApplyedJobModel(models.Model):
    job = models.ForeignKey(JobsModel,on_delete=models.CASCADE)
    user = models.ForeignKey(StudentModel,on_delete=models.CASCADE)
    status = models.CharField(choices=JOB_STATUS,max_length=100,default='pending')
    
    def __str__(self) -> str:
        return self.job.title
from django.db import models
from User.models import StudentModel
from django.contrib.auth.models import User

# Create your models here.



class CompanyModel(models.Model):
    company = models.OneToOneField(User,on_delete=models.CASCADE,related_name='company_profile')
    user_type = models.CharField(max_length=50,default='staff')
    
    def __str__(self) -> str:
        return self.company.username



JOB_TYPE = (
    ("remote","remote"),
    ("parttime","parttime"),
    ("office","office"),
)
def upload_image_to(instance, filename):
    return f'staff/jobs/{instance.company}/{filename}'

class JobsModel(models.Model):
    image = models.ImageField(upload_to=upload_image_to,null=True)
    title = models.CharField(max_length=255,null=True)
    company = models.OneToOneField(CompanyModel,on_delete=models.CASCADE,related_name='job_company')
    type = models.CharField(choices=JOB_TYPE,max_length=100,null=True)
    vaccancies = models.IntegerField(null=True)
    package = models.CharField(max_length=100,null=True)
    experiance = models.FloatField(default=0,null=True)
    description = models.TextField(max_length=500,null=True)
    qualifications = models.TextField(
        blank=True,
        null=True,
        help_text="Enter multiple values separated by commas."
    )
    responsibility =  models.TextField(
        blank=True,
        null=True,
        help_text="Enter multiple values separated by commas."
    )
    
    
    
    def save(self, *args, **kwargs):
        if self.qualifications:
            self.qualifications = [s.strip() for s in self.qualifications.split(',')]
        super().save(*args, **kwargs)
    
    def save(self, *args, **kwargs):
        if self.responsibility:
            self.responsibility = [s.strip() for s in self.responsibility.split(',')]
        super().save(*args, **kwargs)
    
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

class SaveJobModel(models.Model):
    job = models.ForeignKey(JobsModel,on_delete=models.CASCADE)
    user = models.ForeignKey(StudentModel,on_delete=models.CASCADE)
    
    
    
    def __str__(self) -> str:
        return self.job.title
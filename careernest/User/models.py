from django.db import models
from django.contrib.auth.models import User


DEPARTMENT_OPTIONS= (
    ("CSE","COMPUER SCIENCE AND ENGINERRING"),
    ("ECE","ELECTIC AND COMMUNICATION ENGINEERING"),
    ("MECH","MECHANICAL ENGINEERING"),
    ("CIVIL","CIVIL ENGINEERING"),
    ("OTHER","OTHER")
)


def upload_certificate_to(instance, filename):
    return f'certificates/{instance.user.username}/{filename}'

def upload_resume_to(instance, filename):
    return f'resume/{instance.user.username}/{filename}'



class StudentModel(models.Model):
    
    user = models.OneToOneField(User,on_delete=models.CASCADE,related_name='user_profile')
    phone = models.CharField(max_length=10,null=True)
    department = models.CharField(choices = DEPARTMENT_OPTIONS,null=True,max_length=60)
    ten_certificate = models.FileField(upload_to=upload_certificate_to, null=True)
    plustwo_certificate = models.FileField(upload_to=upload_certificate_to, null=True)
    resume = models.FileField(upload_to=upload_resume_to,null=True)
    
    
    
    
    def __str__(self):
        return self.user.username
from django.db import models

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
from email.policy import default
from django.db import models

# Create your models here.
class UserPredictDataModel(models.Model):
    Gender = models.CharField(max_length=100)
    Age = models.CharField(max_length=100)
    EDUC = models.CharField(max_length=100)
    SES = models.CharField(max_length=100)
    MMSE = models.CharField(max_length=100)
    CDR = models.CharField(max_length=100)
    eTIV = models.CharField(max_length=100)
    nWBV = models.CharField(max_length=100)
    ASF = models.CharField(max_length=100)
    output = models.CharField(max_length=100)

    def __str__(self):
        return self.Gender,self.Age,self.EDUC,self.SES,self.MMSE,self.CDR,self.eTIV,self.nWBV,self.ASF,self.output

class DoctorFeedModel(models.Model):
    Feedback = models.TextField(max_length=100)

    def __str__(self):
        return str(self.Feedback)
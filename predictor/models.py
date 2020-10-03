from django.db import models
from datetime import datetime   

# Create your models here.

class Heart(models.Model):
        sno = models.AutoField(primary_key=True)
        name = models.CharField(max_length=50)
        age = models.CharField(max_length=50)
        bp = models.CharField(max_length=50)
        chol = models.CharField(max_length=50)
        beat = models.CharField(max_length=50)
        gender = models.CharField(max_length=50)
        cp = models.CharField(max_length=50)
        fbs = models.CharField(max_length=50)
        restecg = models.CharField(max_length=50)
        exang = models.CharField(max_length=50)
        oldpeak = models.CharField(max_length=50)
        slope = models.CharField(max_length=50)
        ca = models.CharField(max_length=50)
        thal = models.CharField(max_length=50)
        probability = models.CharField(max_length=50)
        result = models.CharField(max_length=50)
        timestamp = models.DateTimeField(default=datetime.now)
    
        def __str__(self):
            return self.name+" ..."
        
class Diabetes(models.Model):
        sno = models.AutoField(primary_key=True)
        name = models.CharField(max_length=50)
        age = models.CharField(max_length=50)
        bp = models.CharField(max_length=50)
        glucose = models.CharField(max_length=50)
        skin = models.CharField(max_length=50)
        bmi = models.CharField(max_length=50)
        pregnancies = models.CharField(max_length=50)
        insulin = models.CharField(max_length=50)
        diab = models.CharField(max_length=50)
        probability = models.CharField(max_length=50)
        result = models.CharField(max_length=50)
        timestamp = models.DateTimeField(default=datetime.now)
    
        def __str__(self):
            return self.name+" ..."

class Feedback(models.Model):
    sno = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    message = models.CharField(max_length=50)
    timestamp = models.DateTimeField(default=datetime.now)

    def __str__(self):
        return self.name+" ..."

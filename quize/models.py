from django.db import models

# Create your models here.

class Exam(models.Model):
    question = models.CharField(max_length=100)
    answer = models.CharField(max_length=100)
    
    class Meta:
         db_table = "Exam"
         app_label = "quize"
 
from django.db import models

# Create your models here.

class Summary(models.Model):
    school_name = models.CharField(max_length=255) 
    sydney_participants = models.IntegerField()
    sydney_percentile = models.IntegerField()
    assessment_area = models.CharField(max_length=255) 
    award = models.CharField(max_length=255)  
    class_name = models.CharField(max_length=255)  
    correct_answer_percentage_per_class = models.DecimalField(max_digits=5, decimal_places=2)
    correct_answer = models.BooleanField()
    student_name = models.CharField(max_length=255)  
    student_score = models.DecimalField(max_digits=5, decimal_places=2)
    subject = models.CharField(max_length=255)  
    category_id = models.IntegerField()
    year_level_name = models.CharField(max_length=100)
    answer_id = models.CharField(max_length=100)  
    correct_answer_id = models.CharField(max_length=100)


from django.db import models


# Create your models here.

class ResultSubmission(models.Model):
    STUDENT_ID = (
        ('201132', '201132'),
        ('301132', '301132'),
        ('401132', '401132'),
        ('501132', '501132'),
        ('601132', '601132'),
    )

    COURSE_ID = (
        ('IIT01', 'IIT01'),
        ('IIT02', 'IIT02'),
        ('IIT03', 'IIT03'),
    )
    student_id = models.CharField(max_length=200, null=True, choices=STUDENT_ID)
    course_id = models.CharField(max_length=200, null=True, choices=COURSE_ID)
    class_test_mark = models.FloatField(null=True)
    final_mark = models.FloatField(null=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.student_id



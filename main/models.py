from django.db import models
import uuid

PRIORITY_CHOICES =[
    ("LOW", "low"),
    ("MEDIUM", "medium"),
    ("HIGH", "high"),
    ]

class task(models.Model):

    emp_checkbox = models.BooleanField(default=False)
    emp_priority = models.CharField(max_length=20, choices = PRIORITY_CHOICES)
    emp_task_name = models.CharField(max_length=50)
    emp_due_date = models.DateField()
    emp_description = models.CharField(max_length=200)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)

    def __str__(self):
        return self.emp_priority
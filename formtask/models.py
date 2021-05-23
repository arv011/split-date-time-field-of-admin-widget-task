from django.db import models
from django.contrib.auth.models import AbstractUser



location_choices = (('Corpoarate Headoffice','Corpoarate Headoffice'),
('Operation department','Operation department' ),
('Work Station','Work Station'),
('marketing division', 'marketing division'))

severity_choices = (
    ('Mild','Mild'),
    ('Moderate','Moderate'),
    ('Severe','Severe'),
    ('Fatel','Fatel'),
)

# Create your models here.
class User(AbstractUser):
    pass
class incident(models.Model):
    location = models.CharField(max_length=30,choices=location_choices,default='Corpoarate Headoffice')
    incident_department = models.TextField(null=True)
    Date_and_time_of_incident = models.DateTimeField()
    incident_location = models.TextField()
    initial_severity = models.CharField(max_length=30,choices=severity_choices,default='Mild')
    Suspected_cause = models.TextField()
    Immidiate_action_taken = models.TextField()
    environmental_incident = models.BooleanField(default=False)
    injury_or_illnes = models.BooleanField(default=False)
    Property_damage = models.BooleanField(default=False)
    Vehicle = models.BooleanField(default=False)
    reported_by = models.CharField(max_length=30,null=True,blank=True)

    
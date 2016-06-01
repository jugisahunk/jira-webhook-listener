from django.db import models

# Create your models here.

class Issue(models.Model):
    event_date = models.DateTimeField('date of issue event')
    event_type = models.CharField(max_length=50)
    event_status_name = models.CharField(max_length=50)
    event_status_jira_id = models.IntegerField()
    event_raw = models.TextField()

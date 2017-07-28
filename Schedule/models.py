import uuid
from django.db import models
from django.urls import reverse

# Create your models here.
class resource(models.Model):
    resourceID = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    resource_name = models.CharField(max_length=255)
    resource_level = models.CharField(max_length=255)
    resource_firm = models.CharField(max_length=25)
    resource_group = models.CharField(max_length=255)

    def __str__(self):
        return self.resource_name

class client(models.Model):
    clientID = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    client_name = models.CharField(max_length=255)
    client_industry = models.CharField(max_length=255)
    client_location = models.CharField(max_length=255)

    def __str__(self):
        return self.client_name

class engagement(models.Model):
    engagementID = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    clientID = models.ForeignKey(client, on_delete=models.CASCADE, default=uuid.uuid4)
    engagement_description = models.CharField(max_length=255)
    engagement_code = models.CharField(max_length=255)

    def __str__(self):
        return self.engagement_description

class assignment(models.Model):
    assignment_week = models.CharField(max_length=255)
    assignment_resource = models.ForeignKey(resource, on_delete=models.CASCADE, null=True)
    assignment_engagement = models.ForeignKey(engagement, on_delete=models.CASCADE, null=True)
    assignment_hours = models.PositiveIntegerField(default=0)
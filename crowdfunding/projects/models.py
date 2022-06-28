from django.db import models
from django.contrib.auth import get_user_model

class Pledge(models.Model):
    amount = models.IntegerField()
    comment = models.CharField(max_length=200)
    anonymous = models.BooleanField()
    project = models.ForeignKey("Project", on_delete=models.CASCADE, related_name="pledges")
    # supporter = models.CharField(max_length=200)
    supporter = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name="supporters_pledges")


class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    location = models.CharField(max_length=200)
    goal = models.IntegerField()
    image = models.URLField()
    date_due = models.DateTimeField()
    is_open = models.BooleanField()
    date_created = models.DateTimeField()
    # owner = models.CharField(max_length=200)
    owner = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name="owner_projects")

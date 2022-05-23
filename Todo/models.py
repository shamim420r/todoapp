from pyexpat import model
from turtle import title
from django.db import models


class Status(models.Model):
    status_name = models.CharField(max_length=20)
    status_id = models.IntegerField()

    def __str__(self):
        return self.status_name


class Tasks(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.TextField(max_length=200, null=True, blank=True)
    description = models.TextField(max_length=1000, null=True, blank=True)
    status = models.ForeignKey(Status, on_delete=models.CASCADE)

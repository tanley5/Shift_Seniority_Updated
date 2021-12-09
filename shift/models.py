from django.db import models
from django.db.models.base import Model
from shiftbid.models import Shiftbid
# Create your models here.


class Shift(models.Model):
    report = models.ForeignKey(Shiftbid, on_delete=models.CASCADE, null=True)
    shift = models.CharField(max_length=100)
    agent_email = models.EmailField(blank=True)
    datetime_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Report: {self.report}; Shift: {self.shift}"

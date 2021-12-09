from django.db import models

from shiftbid.models import Shiftbid
# Create your models here.


class Seniority(models.Model):
    report = models.ForeignKey(Shiftbid, on_delete=models.CASCADE, null=True)
    agent_net_id = models.CharField(max_length=100)
    agent_email = models.EmailField()
    seniority_number = models.PositiveIntegerField()
    datetime_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.agent_net_id

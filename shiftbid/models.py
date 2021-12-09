from django.db import models

# Create your models here.


class Shiftbid(models.Model):
    report_name = models.CharField(
        max_length=250, verbose_name='Report Name', blank=False)
    datetime_created = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.report_name

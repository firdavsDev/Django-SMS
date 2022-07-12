from django.db import models

# Create your models here.
from django.db import models
from django.utils.translation import gettext_lazy as _




class SmsLog(models.Model):
    phone_number = models.CharField(max_length=35)
    text = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)


    class Meta:
        verbose_name = "Log"
        verbose_name_plural = "Logs"
        # ordering = ["-id"]

    def __str__(self):
        return self.phone_number


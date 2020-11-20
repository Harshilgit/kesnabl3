from django.db import models

# Create your models here.

class Condition(models.Model):
    condition_name = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.condition_name

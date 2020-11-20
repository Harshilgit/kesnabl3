from django.db import models

# Create your models here.

class Model(models.Model):
    make = models.ForeignKey('make.Make',on_delete=models.CASCADE, null = True)
    model_name = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.model_name

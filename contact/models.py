from django.db import models

# Create your models here.
class organization(models.Model):
    name = models.CharField(max_length=256)
    website = models.URLField(max_length=256, null=True, blank=True)
    email = models.EmailField(max_length=256, null=True, blank=True)
    address = models.TextField(null=True, blank=True)
    phone_1 = models.CharField(max_length=256)
    industry = models.ForeignKey('industry', on_delete=models.CASCADE, null=True, blank=True)
    notes = models.TextField(null=True, blank=True)
    country = models.ForeignKey('country', on_delete=models.CASCADE, null=True, blank=True)
    state = models.ForeignKey('state', on_delete=models.CASCADE, null=True, blank=True)
    city = models.ForeignKey('city', on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.name


class contact(models.Model):
    name = models.CharField(max_length=256)
    mobile = models.CharField(max_length=256, null=True, blank=True)
    email = models.EmailField(max_length=256, null=True, blank=True)
    dob = models.DateField(null=True, blank=True)
    organization = models.ForeignKey('organization', on_delete=models.CASCADE, null=True, blank=True)
    category = models.ForeignKey('category', on_delete=models.CASCADE, null=True, blank=True)
    role = models.ForeignKey('role', on_delete=models.CASCADE, null=True, blank=True)
    anniversary = models.DateField()
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
    )
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)

    def __str__(self):
        return str(self.name)



class category(models.Model):
    name = models.CharField(max_length=256)
    description = models.TextField(null=True)

    def __str__(self):
        return self.name

class role(models.Model):
    name = models.CharField(max_length=256)
    designation = models.CharField(max_length=256)
    description = models.TextField(null=True)

    def __str__(self):
        return self.name


class country(models.Model):
    name = models.CharField(max_length=256)

    def __str__(self):
        return self.name


class state(models.Model):
    country = models.ForeignKey('country', on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=256)

    def __str__(self):
        return self.name


class city(models.Model):
    country = models.ForeignKey('country', on_delete=models.CASCADE, null=True, blank=True)
    state = models.ForeignKey('state', on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=256)

    def __str__(self):
        return self.name


class industry(models.Model):
    name = models.CharField(max_length=256)

    def __str__(self):
        return self.name

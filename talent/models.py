from pickle import TRUE
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Survey(models.Model):
    role = models.CharField(blank=True, max_length=100, null=TRUE)
    education = models.CharField(blank=True, max_length=100, null=TRUE)
    certification = models.CharField(blank=True, max_length=100, null=TRUE)
    role_important=models.CharField(blank=True, max_length=100, null=TRUE)
    location=models.CharField(blank=True, max_length=100, null=TRUE)
    start_date=models.CharField(blank=True, max_length=100, null=TRUE)
    role_level=models.CharField(blank=True, max_length=100, null=TRUE)
    role_time=models.CharField(blank=True, max_length=100, null=TRUE)
    company_size=models.CharField(blank=True, max_length=100, null=TRUE)
    sponsorship=models.CharField(blank=True, max_length=100, null=TRUE)
    languages=models.CharField(blank=True, max_length=100, null=TRUE)
    specific_industry=models.CharField(blank=True, max_length=100, null=TRUE)
    veteran=models.CharField(blank=True, max_length=100, null=TRUE)
    disability=models.CharField(blank=True, max_length=100, null=TRUE)
    expected_salary=models.CharField(blank=True, max_length=100, null=TRUE)
    owner = models.ForeignKey(User, related_name='survey', on_delete=models.CASCADE, null=TRUE)


class Talent(models.Model):
    first_name = models.CharField('First Name', max_length=30, null=TRUE)
    last_name = models.CharField('Last Name', max_length=30, null=TRUE)
    email = models.EmailField('Email', max_length=100, unique=True, null=TRUE)
    phone_number = models.CharField('Phone Number', max_length=15, null=TRUE)
    website = models.CharField('Website', blank=True, max_length=100, null=TRUE)
    zip_code = models.CharField('Zipe Code', max_length=15, blank=True, null=TRUE)
    survey = models.ForeignKey(Survey, blank=True, on_delete=models.CASCADE, null=TRUE)

    def __str__(self):
        return self.first_name + ' ' + self.last_name


from django.db import models
from django.core import validators

# Create your models here.
class Employee(models.Model):
    eid = models.IntegerField(primary_key=True,
                              validators=[validators.MinValueValidator(1),
                                          validators.MaxValueValidator(200)])
    name = models.CharField(max_length=34)
    email = models.EmailField(validators=[validators.RegexValidator(
        regex='^[A-Za-z0-9].+[@]{1}[a-zA-Z].+[.]{1}com|in|gov|co$'
    )])
    dob = models.DateField()
    gender = models.CharField(max_length=34)
    profile_pic = models.ImageField(upload_to='profile')
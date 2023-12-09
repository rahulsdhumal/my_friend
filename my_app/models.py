from django.db import models

# Create your models here.
class friends(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    date_of_birth = models.DateField(null=True)

class location(models.Model):
    name = models.CharField(max_length=100,null=True)

class company_details(models.Model):
    friend = models.ForeignKey(friends,on_delete=models.CASCADE)
    current_company = models.CharField(max_length=50)
    location = models.ForeignKey(location,on_delete=models.CASCADE)
    position = models.CharField(max_length=100,null=True)
    date_of_joining = models.DateField(null=True)







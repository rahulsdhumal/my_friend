from django.db import models

# Create your models here.
class friend_info(models.Model):
    first_name = models.CharField(max_length=100,null=False)
    last_name = models.CharField(max_length=100,null=False)
    contact = models.BigIntegerField(null=False)
    alternative_contact = models.BigIntegerField(null=True)
    email = models.EmailField(null=False)
    date_of_birth = models.DateField(null=False)
    address = models.CharField(max_length=200,null=False)
    maritial_status = models.BooleanField(null=False)
    favorite_sports = models.CharField(max_length=200,null=True)
    hobbies = models.CharField(max_length=200,null=True)


class location(models.Model):
    name = models.CharField(max_length=100,null=False)

class current_company_info(models.Model):
    company_name = models.CharField(max_length=50,null=False)
    location = models.ForeignKey(location,on_delete=models.CASCADE)
    date_of_joining = models.DateField(null=False)
    last_day_date = models.DateField(null=True)
    position = models.CharField(max_length=100,null=False)
    friend = models.ForeignKey(friend_info,on_delete=models.CASCADE)
    grade_out_of_10 = models.IntegerField(null=True)

class old_company_info(models.Model):
    company_name = models.CharField(max_length=50,null=False)
    location = models.ForeignKey(location,on_delete=models.CASCADE)
    date_of_joining = models.DateField(null=False)
    last_day_date = models.DateField(null=False)
    position = models.CharField(max_length=100,null=False)
    friend = models.ForeignKey(friend_info,on_delete=models.CASCADE)
    grade_out_of_10 = models.IntegerField(null=True)
    reason_for_switch = models.CharField(max_length=500,null=True)

class biodata(models.Model):
    resume = models.FileField(null=False)
    friend = models.ForeignKey(friend_info,on_delete=models.CASCADE)

class count_total_exp(models.Model):
    friend = models.ForeignKey(friend_info,on_delete=models.CASCADE)
    current_company = models.ForeignKey(current_company_info,on_delete=models.CASCADE)
    old_company = models.ForeignKey(old_company_info,on_delete=models.CASCADE)
    total_exp = models.CharField(max_length=200,null=False)

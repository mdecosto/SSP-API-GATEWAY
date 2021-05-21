from django.db import models

class UserRole(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=300)

class Account(models.Model):
    userrole = models.ForeignKey('UserRole', on_delete=models.CASCADE)
    is_active = models.BooleanField()
    customer = models.CharField(max_length=100, null=True)
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    
class Keys(models.Model):
    account = models.ForeignKey('Account', on_delete=models.CASCADE)
    publickey = models.TextField(max_length=300)
    expiredate =  models.DateTimeField()
    activedate = models.DateTimeField()
    
class Logs(models.Model):
    account = models.ForeignKey('Account', on_delete=models.CASCADE)
    request = models.TextField(max_length=300)
    response = models.TextField(max_length=300)
    
class BaseModel(models.Model):
    created_by = models.ForeignKey('Account', related_name='created_by', on_delete=models.PROTECT,)
    modified_by = models.ForeignKey('Account', related_name='modified_by', on_delete=models.PROTECT,)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now_add=True)
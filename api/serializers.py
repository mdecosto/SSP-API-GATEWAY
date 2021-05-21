from django.db import models
from rest_framework import serializers
from rest_framework.utils import field_mapping
from .models import UserRole, Account, Keys, Logs, BaseModel

class UserRoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserRole
        fields = ['name', 'description']
        
class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = ['userrole', 'is_active', 'customer', 'username', 'password']
        extra_kwargs = {'password':{'write_only': True}}
        
class KeysSerializer(serializers.ModelSerializer):
    class Meta:
        model = Keys
        fields = ['account', 'publickey', 'expiredate', 'activedate']
        
class LogsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Logs
        fields = ['account', 'request', 'response']
        
class BaseModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = BaseModel
        fields = ['created_by', 'modified_by', 'created_at', 'modified_at']
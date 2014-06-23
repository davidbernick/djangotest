from rest_framework import serializers
from django.contrib.auth.models import User, Group, Permission

from .models import Task,Category

class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('id', 'username', 'first_name', 'last_name','email' )

class CategorySerializer(serializers.ModelSerializer):
    name = serializers.CharField(max_length=100)    
    class Meta:
        model = Category
        #fields = ('name')

class TasksSerializer(serializers.ModelSerializer):
    reported_by = UserSerializer(required=False)
    categories = CategorySerializer(many=True,required=False)
    read_only_fields = ('categories')

    class Meta:
        model = Task

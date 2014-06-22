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
    categories = CategorySerializer()

    def get_fields(self, *args, **kwargs):
        fields = super(TasksSerializer, self).get_fields(*args, **kwargs)
        request = self.context.get('request', None)
        view = self.context.get('view', None)

        if (request and view and getattr(view, 'object', None) and
                request.user == view.object.user):
            fields['categories'].read_only = True

        return fields

    class Meta:
        model = Task
